#!/usr/bin/env python3
"""Kiểm tra quy ước tài liệu trong stories/. Exit 1 nếu có lỗi.

--base <ref>: kiểm tra thêm thay đổi so với <ref> (dùng trong CI cho PR).
"""
import argparse
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STORIES = ROOT / "stories"
STATUSES = ["draft", "review", "ready", "in-dev", "uat", "done", "cancelled"]
BRD_STATUSES = ["draft", "review", "approved"]
FROZEN = {"done", "cancelled"}
FULL_COVERAGE = {"uat", "done"}

ID = r"[A-Z][A-Z0-9]+-\d+"
FOLDER_RE = re.compile(rf"^({ID})-[a-z0-9]+(?:-[a-z0-9]+)*$")
BRD_FILE_RE = re.compile(r"^B(\d+)-[a-z0-9]+(?:-[a-z0-9]+)*\.md$")
HANDOFF_RE = re.compile(r"^\d{4}-\d{2}-\d{2}-[a-z0-9]+(?:-[a-z0-9]+)*\.md$")
REQ_HEAD = re.compile(rf"^#{{2,4}}\s+({ID}-B\d+-R\d+)\b")
AC_DEF = re.compile(rf"^\s*[-*]\s+\*\*({ID}-B\d+-R\d+-AC\d+)\*\*")
TC_HEAD = re.compile(rf"^#{{2,4}}\s+({ID}-B\d+-TC\d+)\b")
COVERS = re.compile(r"^\s*[-*]?\s*covers:\s*(.+)$", re.I)
ANY_REF = re.compile(rf"\b{ID}-B\d+-R\d+(?:-AC\d+)?\b")

errors, warnings = [], []


def rel(p):
    try:
        return str(Path(p).relative_to(ROOT))
    except ValueError:
        return str(p)


def err(p, msg):
    errors.append(f"{rel(p)}: {msg}")


def warn(p, msg):
    warnings.append(f"{rel(p)}: {msg}")


def read(p):
    return p.read_text(encoding="utf-8")


def frontmatter(text):
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    if end == -1:
        return {}
    fm = {}
    for line in text[3:end].splitlines():
        if ":" in line and not line.lstrip().startswith("#"):
            k, v = line.split(":", 1)
            fm[k.strip()] = re.split(r"\s+#", v, maxsplit=1)[0].strip()
    return fm


def md_files(folder):
    return sorted(folder.glob("*.md")) if folder.is_dir() else []


def check_brd_file(f, key, seen_brd, all_reqs, acs):
    m = BRD_FILE_RE.match(f.name)
    if not m:
        err(f, "tên file phải là B<n>-<slug>.md")
        return None
    n = m.group(1)
    if n in seen_brd:
        err(f, f"trùng số B{n} với {rel(seen_brd[n])}")
    seen_brd[n] = f
    text = read(f)
    fm = frontmatter(text)
    if fm.get("id") != f"{key}-B{n}":
        err(f, f"frontmatter id phải là {key}-B{n}")
    if fm.get("status") not in BRD_STATUSES:
        err(f, f"status '{fm.get('status')}' không hợp lệ: {' | '.join(BRD_STATUSES)}")

    prefix = f"{key}-B{n}-R"
    reqs, cur = {}, None
    for i, line in enumerate(text.splitlines(), 1):
        if rm := REQ_HEAD.match(line):
            cur = rm.group(1)
            if not cur.startswith(prefix):
                err(f, f"dòng {i}: {cur} phải bắt đầu bằng {prefix}")
            if cur in all_reqs:
                err(f, f"dòng {i}: {cur} trùng với {rel(all_reqs[cur])}")
            all_reqs[cur] = f
            reqs[cur] = 0
        elif am := AC_DEF.match(line):
            ac = am.group(1)
            if cur is None or not ac.startswith(cur + "-AC"):
                err(f, f"dòng {i}: {ac} phải nằm dưới yêu cầu {ac.rsplit('-AC', 1)[0]}")
                continue
            if ac in acs:
                err(f, f"dòng {i}: {ac} trùng")
            acs[ac] = f
            reqs[cur] += 1
    for r, count in reqs.items():
        if count == 0:
            err(f, f"{r} chưa có acceptance criteria (**{r}-AC1**: …)")
    if not reqs:
        warn(f, "chưa có yêu cầu nào")
    return n


def check_tests(d, key, acs):
    covered = set()
    for f in md_files(d / "test"):
        m = BRD_FILE_RE.match(f.name)
        if not m:
            err(f, "tên file phải là B<n>-<slug>.md")
            continue
        prefix = f"{key}-B{m.group(1)}-TC"
        seen = set()
        for i, line in enumerate(read(f).splitlines(), 1):
            if tm := TC_HEAD.match(line):
                tc = tm.group(1)
                if not tc.startswith(prefix):
                    err(f, f"dòng {i}: {tc} phải bắt đầu bằng {prefix}")
                if tc in seen:
                    err(f, f"dòng {i}: {tc} trùng")
                seen.add(tc)
            elif cm := COVERS.match(line):
                for ref in re.split(r"[,\s]+", cm.group(1).strip()):
                    if not ref:
                        continue
                    if ref not in acs:
                        err(f, f"dòng {i}: covers {ref} không tồn tại")
                    covered.add(ref)
    return covered


def check_story(d, all_reqs):
    m = FOLDER_RE.match(d.name)
    if not m:
        err(d, "tên folder phải là <KEY>-<slug> (key tracker + chữ thường không dấu, gạch ngang)")
        return
    key = m.group(1)

    for name in ("README.md", "CHANGELOG.md", "decisions.md"):
        if not (d / name).is_file():
            err(d, f"thiếu {name}")
    brd_files = md_files(d / "requirements")
    if not brd_files:
        err(d, "requirements/ cần ít nhất 1 file B<n>-<slug>.md")

    for f in d.rglob("*.md"):
        if "{{" in read(f):
            err(f, "còn placeholder {{…}}")

    status = None
    readme = d / "README.md"
    if readme.is_file():
        fm = frontmatter(read(readme))
        if fm.get("key") != key:
            err(readme, f"frontmatter key phải là {key}")
        status = fm.get("status")
        if status not in STATUSES:
            err(readme, f"status '{status}' không hợp lệ: {' | '.join(STATUSES)}")
        owner = fm.get("owner", "")
        if not owner or owner.startswith("["):
            warn(readme, "chưa có owner")

    acs, seen_brd = {}, {}
    for f in brd_files:
        check_brd_file(f, key, seen_brd, all_reqs, acs)

    for part in ("design", "test"):
        for f in md_files(d / part):
            bm = BRD_FILE_RE.match(f.name)
            if bm and bm.group(1) not in seen_brd:
                err(f, f"không có BRD B{bm.group(1)} tương ứng trong requirements/")

    covered = check_tests(d, key, acs)
    missing = sorted(set(acs) - covered)
    if missing:
        msg = f"{len(missing)} AC chưa có testcase: {', '.join(missing)}"
        if status in FULL_COVERAGE:
            err(d, msg + f" (bắt buộc từ status {'/'.join(sorted(FULL_COVERAGE))})")
        elif status == "in-dev":
            warn(d, msg)

    for f in md_files(d / "design"):
        for ref in set(ANY_REF.findall(read(f))):
            if ref not in acs and ref not in all_reqs:
                warn(f, f"tham chiếu {ref} không tồn tại")

    for f in (d / "handoffs").glob("*") if (d / "handoffs").is_dir() else []:
        if f.name != ".gitkeep" and not HANDOFF_RE.match(f.name):
            err(f, "tên file phải là YYYY-MM-DD-<từ>-to-<đến>.md")


def git(*args):
    return subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True, encoding="utf-8")


def check_diff(base):
    mb = git("merge-base", base, "HEAD")
    if mb.returncode != 0:
        warn(ROOT, f"không tìm được merge-base với {base}, bỏ qua kiểm tra diff")
        return
    mb = mb.stdout.strip()
    changed = git("diff", "--name-only", mb, "HEAD").stdout.splitlines()
    by_story = {}
    for p in changed:
        parts = p.split("/")
        if parts[0] == "stories" and len(parts) >= 3:
            by_story.setdefault(parts[1], set()).add("/".join(parts[2:]))
    for story, files in sorted(by_story.items()):
        d = STORIES / story
        if any(f.startswith("requirements/") for f in files) and "CHANGELOG.md" not in files:
            err(d, "sửa requirements/ nhưng chưa ghi CHANGELOG.md")
        old = git("show", f"{mb}:stories/{story}/README.md")
        if old.returncode == 0 and frontmatter(old.stdout).get("status") in FROZEN:
            err(d, "Story đã done/cancelled, không sửa. Tạo Story mới, link về Story này")


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--base", help="ref để so sánh, vd origin/main")
    a = p.parse_args()

    all_reqs = {}
    stories = [d for d in sorted(STORIES.iterdir()) if d.is_dir() and not d.name.startswith(".")] if STORIES.is_dir() else []
    for d in stories:
        check_story(d, all_reqs)
    if a.base:
        check_diff(a.base)

    for w in warnings:
        print(f"CẢNH BÁO  {w}")
    for e in errors:
        print(f"LỖI       {e}")
    print(f"\n{len(stories)} Story · {len(all_reqs)} REQ · {len(errors)} lỗi · {len(warnings)} cảnh báo")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
