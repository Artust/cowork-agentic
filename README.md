# Repo tài liệu

Nguồn sự thật cho yêu cầu, thiết kế, quyết định, testcase. Code ở repo riêng: `[URL repo code]`.
Chat để bàn; chốt thì về đây qua PR.

## Cấu trúc

```
_shared/        dùng chung nhiều Story
  constitution.md   nguyên tắc bắt buộc, DoR/DoD
  constraints.md    constraints register (V3)
  architecture.md   tổng quan hệ thống (V3)
  glossary.md
  decisions/        ADR liên Story
process/        02 team context · 03 prompts · 04 learning log
skills/         skill dùng chung (chuẩn agentskills.io)
templates/      khung Story, handoff, PR repo code
scripts/        new.py (tạo) · check_docs.py (kiểm tra, chạy trong CI)
stories/<KEY>-<slug>/
  README.md         trạng thái, BRD/phần, đang chờ, câu hỏi mở
  requirements/     B1-<slug>.md, B2-…  (1 Story nhiều BRD)
  design/           B1-<slug>.md …      (1 file / BRD)
  test/             B1-<slug>.md …      (1 file / BRD)
  handoffs/         YYYY-MM-DD-<từ>-to-<đến>.md
  decisions.md
  CHANGELOG.md
```

`stories/DEMO-1-dang-nhap-otp/` là ví dụ. Xóa khi bắt đầu dùng thật (xóa cả C-001 ví dụ trong `_shared/constraints.md`).

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

## Trạng thái Story

`draft → review → ready → in-dev → uat → done | cancelled`

`done`, `cancelled` = đóng băng. Thay đổi sau đó → Story mới, link về Story cũ.

## Flow 8 bước → repo

| Bước | Làm gì ở đây |
|---|---|
| 1 Research | Phát hiện ràng buộc → `_shared/constraints.md`; kiến thức → `process/04-learning-log.md` |
| 2 BRD | `new.py story` / `new.py brd`; viết REQ + AC; chạy V3 với `_shared/constraints.md`, `architecture.md` |
| 3 Design | `design/B<n>-…md`; quyết định → `decisions.md` |
| 4 Review | PR, reviewer theo `CODEOWNERS`. Sai → quay lại bước 2, ghi `Changed` vào CHANGELOG |
| 5 Execute | `test/B<n>-…md` song song dev; status `in-dev`; PR code ghi REQ ID, link vào `code_prs` |
| 6 UAT | status `uat` (CI bắt buộc mọi AC có testcase) |
| 7 Fix bug | Bug trên tracker, ghi REQ ID. Đổi REQ → CHANGELOG |
| 8 Deploy | status `done` → đóng băng |

Mỗi lần chuyển bước: `new.py handoff`, điền theo prompt V1. Cuối mỗi phiên chat: chạy V2, dán vào `decisions.md` / `CHANGELOG.md`.

## Thao tác

```bash
python scripts/new.py story PROJ-123 dang-nhap-otp "Đăng nhập bằng OTP" --owner "BA-An"
python scripts/new.py brd stories/PROJ-123-dang-nhap-otp khoa-tai-khoan "Khóa tài khoản" --owner "BA-An"
python scripts/new.py handoff stories/PROJ-123-dang-nhap-otp ba dev
python scripts/check_docs.py                  # toàn repo
python scripts/check_docs.py --base origin/main   # + kiểm tra diff như CI
```

BA, Designer: sửa file trên giao diện web GitHub/GitLab → tạo PR. Không cần command line.

## Quy tắc

- Mọi thay đổi qua PR. Reviewer tự gán theo `CODEOWNERS`.
- `CHANGELOG.md` chỉ thêm dòng.
- Quyết định `accepted` không sửa; thêm quyết định mới `supersedes`.
- Link, không chép: Figma, code, `_shared/` chỉ link tới.
- Không commit PII, dữ liệu khách hàng, secret. Ảnh chụp Figma dùng dữ liệu giả.
- File không ai đọc sau 2 Story → gộp hoặc bỏ.
