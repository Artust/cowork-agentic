# Repo tài liệu

Nguồn sự thật cho yêu cầu, thiết kế, quyết định, testcase. Code ở repo riêng: `[URL repo code]`.
Chat để bàn; chốt thì về đây.

Đang chạy **E1 — bản tối giản** trên 1 Story (`process/02-team-context.md`). Chỉ mục "Bắt buộc" là bắt buộc. Phần còn lại tùy chọn; đo xong mới quyết giữ hay bỏ.

## Bắt buộc (E1)

| Ai | Làm gì | Ở đâu |
|---|---|---|
| BA | README Story + BRD: REQ, AC | `stories/<KEY>/README.md`, `requirements/B1-….md` |
| Người chốt | Mỗi quyết định 1 mục | `stories/<KEY>/decisions.md` |
| Tester | Testcase, mỗi case ghi `covers:` AC | `stories/<KEY>/test/B1-….md` |
| Người gửi | Handoff ở 2 mốc: BRD → Design/Dev · Dev → UAT | `stories/<KEY>/handoffs/` |
| Mọi PR | Tick dòng "Output AI" | PR template |

Tùy chọn: `design/`, `CHANGELOG.md`, handoff ở mốc khác, ADR, skill. `CHANGELOG.md` bắt buộc 1 dòng khi đổi REQ/AC sau khi BRD `approved`.

## Ai đọc gì

| Vai trò | Đọc | Việc trong repo |
|---|---|---|
| BA | Mục trên + `templates/story/requirements/BRD.md` | Viết BRD; đổi status Story sang `review` |
| Designer | Mục trên + `templates/story/design/BRD.md` | Điền `figma`, `figma_version`, bảng frame trước Review. Không cần gì khác |
| Dev | Cả file này + `AGENTS.md` | V3 khả thi; handoff → UAT; chạy `scripts/`; link `code_prs` |
| Tester | Mục trên + `templates/story/test/BRD.md` | Testcase từ AC; đổi status sang `uat` |

BA, Designer, Tester sửa file trên giao diện web GitHub/GitLab. Cần `new.py` → nhờ Dev.

## Cấu trúc

```
_shared/        dùng chung nhiều Story
  constraints.md    constraints register (V3)
  architecture.md   tổng quan hệ thống (V3), điền dần
  glossary.md
  decisions/        ADR liên Story, cùng format decisions.md
process/        02 team context · 03 prompts · 04 learning log · project-instructions
skills/         skill dùng chung (chuẩn agentskills.io)
templates/      khung Story, handoff, PR repo code
scripts/        new.py (tạo) · check_docs.py (kiểm tra, chạy trong CI)
stories/<KEY>-<slug>/
  README.md         trạng thái, BRD/phần, đang chờ, câu hỏi mở
  requirements/     B1-<slug>.md, B2-…  (1 Story nhiều BRD)
  decisions.md
  test/             B1-<slug>.md …
  handoffs/         YYYY-MM-DD-<từ>-to-<đến>.md
  design/           B1-<slug>.md …      (tùy chọn)
  CHANGELOG.md                          (tùy chọn)
```

`AGENTS.md`: chỉ dẫn cho AI. `CLAUDE.md` chỉ chứa `@AGENTS.md` để Claude Code đọc cùng nội dung.
`stories/DEMO-1-dang-nhap-otp/` là ví dụ. Xóa khi dùng thật (xóa cả C-001 ví dụ trong `_shared/constraints.md`).

## ID

| Loại | Mẫu | Ví dụ |
|---|---|---|
| Story | key tracker | `PROJ-123` |
| BRD | `<KEY>-B<n>` | `PROJ-123-B2` |
| Yêu cầu | `<KEY>-B<n>-R<nn>` | `PROJ-123-B2-R01` |
| Acceptance criteria | `<REQ>-AC<n>` | `PROJ-123-B2-R01-AC1` |
| Testcase | `<KEY>-B<n>-TC<nn>` | `PROJ-123-B2-TC03` |
| Quyết định Story | `<KEY>-D<nn>` | `PROJ-123-D04` |
| Quyết định liên Story | `ADR-<nnnn>` | `ADR-0007` |
| Ràng buộc | `C-<nnn>` | `C-012` |

Task trên tracker ghi ID BRD/REQ. PR repo code ghi REQ ID (mẫu: `templates/code-repo/`).

## Trạng thái

Story: `draft → review → ready → in-dev → uat → done | cancelled` · BRD: `draft | approved`

| Story sang | Ai đổi | Điều kiện |
|---|---|---|
| `review` | BA | BRD có REQ + AC; PR đang mở |
| `ready` | Dev (reviewer) | Đã đối chiếu `_shared/constraints.md` (V3); REQ rủi ro cao Dev xác nhận; câu hỏi mở có người trả lời + hạn; BRD `approved` |
| `in-dev` | Dev | Có handoff BRD → Dev |
| `uat` | Tester | Mọi AC có testcase, đã chạy; có handoff Dev → UAT |
| `done` | BA/PO | Đã deploy; `code_prs` đã link |

`done`, `cancelled` = đóng băng: chỉ còn sửa frontmatter và link trong README Story. Thay đổi khác → Story mới, link về Story cũ.

## Flow 8 bước → repo

| Bước | Làm gì ở đây |
|---|---|
| 1 Research | Ràng buộc → `_shared/constraints.md`; kiến thức → `process/04-learning-log.md` |
| 2 BRD | `new.py story` / `new.py brd`; viết REQ + AC; chạy V3 với `_shared/constraints.md`, `architecture.md` |
| 3 Design | Figma;html; `design/B<n>-….md` (tùy chọn); quyết định → `decisions.md` |
| 4 Review | PR, reviewer theo `CODEOWNERS`. Sai → quay lại bước 2, ghi `Changed` vào CHANGELOG |
| 5 Execute | Handoff BRD → Dev; `test/B<n>-….md` song song dev; status `in-dev`; PR code ghi REQ ID, link vào `code_prs` |
| 6 UAT | Handoff Dev → UAT; status `uat` |
| 7 Fix bug | Bug trên tracker, ghi REQ ID. Đổi REQ → CHANGELOG |
| 8 Deploy | status `done` → đóng băng |

Cuối phiên chat **có quyết định**: chạy V2, dán vào `decisions.md` (và CHANGELOG nếu đổi REQ).

## Thao tác

```bash
python scripts/new.py story PROJ-123 dang-nhap-otp "Đăng nhập bằng OTP" --owner "BA-An"
python scripts/new.py brd stories/PROJ-123-dang-nhap-otp khoa-tai-khoan "Khóa tài khoản" --owner "BA-An"
python scripts/new.py handoff stories/PROJ-123-dang-nhap-otp ba dev
python scripts/check_docs.py                     # E1: chỉ chặn lỗi nặng
python scripts/check_docs.py --strict            # sau 2 Story
python scripts/check_docs.py --base origin/main  # + kiểm tra diff như CI
```

## Quy tắc

- PR bắt buộc: `requirements/`, `decisions.md`, `_shared/`, `skills/`, `scripts/`, `AGENTS.md`, `CLAUDE.md`. Reviewer theo `CODEOWNERS`.
- Commit thẳng được: `handoffs/`, `test/`, `design/`, mục "Đang chờ" và "Câu hỏi mở" trong README Story. Quy ước, không chặn bằng branch protection (branch protection áp cả repo).
- Đổi REQ/AC sau khi BRD `approved` → 1 dòng `CHANGELOG.md`, ghi quyết định.
- Quyết định `accepted` không sửa; thêm quyết định mới ghi `supersedes`.
- Link, không chép: Figma, code, `_shared/` chỉ link tới.
- Không commit PII, dữ liệu khách hàng, secret. Ảnh Figma dùng dữ liệu giả.
- File không ai đọc sau 2 Story → gộp hoặc bỏ. Xét ở retro cuối sprint.

## CI

`check_docs.py` mặc định chỉ chặn: trùng ID, còn placeholder `{{…}}`, sai tên folder Story, sửa Story đã đóng băng. Vi phạm khác → cảnh báo.
Sau 2 Story: thêm `--strict` vào `.github/workflows/docs-check.yml` (và `.gitlab-ci.yml`).
Branch protection cho `main` trong E1: không bật "Require a pull request". CI chạy trên PR và trên push `main`; lỗi hiện đỏ.

## Dùng với Claude

- **Claude chat (Project):** Project knowledge → "+" → GitHub → repo này. Chọn `README.md`, `AGENTS.md`, `process/`, `_shared/`, `templates/`, Story đang làm. Đổi lựa chọn bằng "Configure files"; bấm Sync sau mỗi lần merge. Project instructions: dán từ `process/project-instructions.md`.
- **Claude Code:** clone repo, làm trên branch, mở PR. Đọc `CLAUDE.md` → `AGENTS.md`.
- Lịch sử chat không sang được công cụ khác. Thứ cần giữ → V2 → file.

## Đo (E1)

Baseline từ Story hiện tại, đo lại sau 1 Story: số lần hỏi lại điều đã chốt · quyết định trong chat vs trong `decisions.md` · thời gian từ lúc chốt trong chat → có trong file · phút/người/ngày duy trì repo.
Dừng: > 15 phút/người/ngày, hoặc < 50% quyết định vào file sau 2 tuần → cắt tiếp (bỏ CHANGELOG tay, lấy từ tiêu đề PR).
