#!/usr/bin/env python3
"""Tạo Story, BRD, handoff từ templates/."""
import argparse
import datetime
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TPL = ROOT / "templates"
STORIES = ROOT / "stories"
KEY_RE = re.compile(r"^[A-Z][A-Z0-9]+-\d+$")
SLUG_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
BRD_FILE_RE = re.compile(r"^B(\d+)-")
TODAY = datetime.date.today().isoformat()


def die(msg):
    sys.exit(f"LỖI: {msg}")


def fill(text, vals):
    for k, v in vals.items():
        text = text.replace("{{" + k + "}}", v)
    return text


def write(src, dst, vals):
    if dst.exists():
        die(f"đã tồn tại: {dst.relative_to(ROOT)}")
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_text(fill(src.read_text(encoding="utf-8"), vals), encoding="utf-8")
    print(f"+ {dst.relative_to(ROOT)}")


def check_slug(slug):
    if not SLUG_RE.match(slug):
        die(f"slug '{slug}' phải là chữ thường không dấu, số, gạch ngang")


def story_dir_and_key(path):
    d = Path(path).resolve()
    if not d.is_dir():
        die(f"không thấy folder {path}")
    m = re.match(r"^([A-Z][A-Z0-9]+-\d+)-", d.name)
    if not m:
        die(f"tên folder {d.name} không đúng <KEY>-<slug>")
    return d, m.group(1)


def brd_files(d, n, vals, parts):
    for part in parts:
        write(TPL / "story" / part / "BRD.md", d / part / f"B{n}-{vals['BRD_SLUG']}.md", vals)


def add_changelog(d, line):
    f = d / "CHANGELOG.md"
    if not f.is_file():
        return
    lines = f.read_text(encoding="utf-8").splitlines()
    head = f"## {TODAY}"
    idx = next((i for i, l in enumerate(lines) if l.startswith("## ")), None)
    if idx is None:
        lines += ["", head, line]
    elif lines[idx] == head:
        lines.insert(idx + 1, line)
    else:
        lines[idx:idx] = [head, line, ""]
    f.write_text("\n".join(lines) + "\n", encoding="utf-8")


def add_brd_row(d, row):
    f = d / "README.md"
    lines = f.read_text(encoding="utf-8").splitlines()
    try:
        i = next(i for i, l in enumerate(lines) if l.strip() == "## BRD / phần")
    except StopIteration:
        print("! README thiếu mục '## BRD / phần', tự thêm dòng BRD")
        return
    j = i + 1
    while j < len(lines) and not lines[j].startswith("|"):
        j += 1
    while j < len(lines) and lines[j].startswith("|"):
        j += 1
    lines.insert(j, row)
    f.write_text("\n".join(lines) + "\n", encoding="utf-8")


def cmd_story(a):
    if not KEY_RE.match(a.key):
        die(f"key '{a.key}' phải dạng PROJ-123")
    check_slug(a.slug)
    brd_slug = a.brd_slug or a.slug
    check_slug(brd_slug)
    d = STORIES / f"{a.key}-{a.slug}"
    if d.exists():
        die(f"đã tồn tại: {d.relative_to(ROOT)}")
    vals = {"KEY": a.key, "TITLE": a.title, "OWNER": a.owner, "DATE": TODAY,
            "BRD": "B1", "BRD_SLUG": brd_slug, "BRD_TITLE": a.brd_title or a.title}
    # E1: bắt buộc README, decisions, requirements, test. CHANGELOG, design tùy chọn (--full)
    files = ["README.md", "decisions.md"] + (["CHANGELOG.md"] if a.full else [])
    for f in files:
        write(TPL / "story" / f, d / f, vals)
    brd_files(d, 1, vals, ["requirements", "test"] + (["design"] if a.full else []))
    (d / "handoffs").mkdir()
    (d / "handoffs" / ".gitkeep").touch()
    print(f"+ {(d / 'handoffs').relative_to(ROOT)}/")


def cmd_brd(a):
    d, key = story_dir_and_key(a.story)
    check_slug(a.slug)
    nums = [int(m.group(1)) for f in (d / "requirements").glob("B*.md")
            if (m := BRD_FILE_RE.match(f.name))]
    n = max(nums, default=0) + 1
    vals = {"KEY": key, "OWNER": a.owner, "DATE": TODAY,
            "BRD": f"B{n}", "BRD_SLUG": a.slug, "BRD_TITLE": a.title}
    brd_files(d, n, vals, ["requirements", "test"] + (["design"] if a.full else []))
    add_brd_row(d, f"| [{key}-B{n}](requirements/B{n}-{a.slug}.md) | {a.title} | [ ] | {a.owner} | draft |")
    add_changelog(d, f"- Added {key}-B{n}: tạo BRD \"{a.title}\".")
    print("~ README.md cập nhật")


def cmd_handoff(a):
    d, key = story_dir_and_key(a.story)
    check_slug(a.frm)
    check_slug(a.to)
    vals = {"KEY": key, "FROM": a.frm, "TO": a.to, "DATE": TODAY}
    write(TPL / "handoff.md", d / "handoffs" / f"{TODAY}-{a.frm}-to-{a.to}.md", vals)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    sub = p.add_subparsers(required=True)

    s = sub.add_parser("story", help="tạo Story mới kèm BRD B1")
    s.add_argument("key", help="key tracker, vd PROJ-123")
    s.add_argument("slug", help="vd dang-nhap-otp")
    s.add_argument("title")
    s.add_argument("--owner", default="[?]")
    s.add_argument("--brd-slug", help="slug BRD đầu tiên (mặc định = slug Story)")
    s.add_argument("--brd-title", help="tên BRD đầu tiên (mặc định = title)")
    s.add_argument("--full", action="store_true", help="tạo cả CHANGELOG.md, design/ (ngoài bộ tối giản E1)")
    s.set_defaults(func=cmd_story)

    b = sub.add_parser("brd", help="thêm BRD vào Story")
    b.add_argument("story", help="đường dẫn folder Story")
    b.add_argument("slug")
    b.add_argument("title")
    b.add_argument("--owner", default="[?]")
    b.add_argument("--full", action="store_true", help="tạo cả design/")
    b.set_defaults(func=cmd_brd)

    h = sub.add_parser("handoff", help="tạo file bàn giao")
    h.add_argument("story", help="đường dẫn folder Story")
    h.add_argument("frm", metavar="from", help="vd ba")
    h.add_argument("to", help="vd dev")
    h.set_defaults(func=cmd_handoff)

    a = p.parse_args()
    a.func(a)


if __name__ == "__main__":
    main()
