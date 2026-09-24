# Team context — AI trong phát triển phần mềm
Cập nhật: 2026-09-24 · Người giữ file: [?]
`[?]` = chưa có thông tin, cần điền.

## Team
- Vai trò: BA, Designer, Dev, Tester, [PM/PO?]
- Quy mô: [?] người · Làm việc: [onsite / remote / hybrid]
- Sản phẩm, domain: [?]
- Loại dự án: [greenfield / brownfield / outsourcing]
- Stack: [?]
- Công cụ: issue tracker [?] · tài liệu: repo git riêng `github.com/Artust/cowork-agentic` (private) · repo code [?] · design Figma · chat [?]
- AI đang dùng: Claude (chat, Project) · khác [?] · Ai có license: [?]
- Chính sách dữ liệu: [được / không đưa code, dữ liệu khách hàng vào AI]

## Đơn vị công việc
Story → nhiều BRD (mỗi BRD 1 phần) → nhiều task trên tracker.
Quy ước folder, ID, trạng thái: `README.md` repo tài liệu. Thuật ngữ: `_shared/glossary.md`.

## Flow hiện tại
| # | Bước | Tham gia | Output | Nơi lưu (repo tài liệu) |
|---|------|----------|--------|--------|
| 1 | Research | BA + Dev | [?] | `_shared/constraints.md`, `process/04-learning-log.md` |
| 2 | BRD | Cả team | BRD | `stories/<KEY>/requirements/B<n>-….md` |
| 3 | Design: wireframe/Figma + design detail của Dev | Designer + BA + Dev + Test | Figma, design detail | `design/B<n>-….md` (link Figma,html, tùy chọn), `decisions.md` |
| 4 | Review: sai sót → quay lại 2, ổn → đi tiếp | Cả team | [?] | PR, reviewer theo `CODEOWNERS` |
| 5 | Execute: develop + viết testcase | Dev + Test | Code, testcase | `test/B<n>-….md`; code ở repo code |
| 6 | UAT | [?] | [?] | status `uat` |
| 7 | Fix bug | [?] | | tracker, ghi REQ ID |
| 8 | Deploy | [?] | | status `done` (đóng băng) |

Chuyển bước → `stories/<KEY>/handoffs/` (V1). Cuối phiên chat có quyết định → `decisions.md`, `CHANGELOG.md` (V2).

## Vấn đề
- **P1 — Mất context khi chuyển bước.** Người xử lý không nắm hết hoặc quên.
- **P2 — Giới hạn công nghệ phát hiện muộn.** Phải sửa lại BRD hoặc design.
- **P3 — Thông tin phân mảnh.** Update liên tục sinh nhiều chat/thread trong workspace → sót, mất thông tin.

## Mục tiêu
- Mọi vai trò dùng AI để tăng tốc độ phát triển.
- Chỉ số muốn cải thiện: [lead time ý tưởng → deploy · số lần quay lại bước 2 · bug lọt tới UAT · giờ viết BRD, testcase]
- Baseline: [?]
- Cách đo không thêm bước: PR template ghi output AI (nguyên / sửa nhẹ / viết lại) · diff bản AI nháp vs bản cuối · `scripts/check_docs.py`.

## Giả thuyết đang xét (chưa kiểm chứng)
- **H1 → P3.** Nguồn sự thật = repo tài liệu git, mỗi Story 1 folder: BRD · design · decision log · change log. Chat, memory của agent không phải nguồn sự thật; phiên có quyết định thì ghi về file (V2). *Đã chọn cấu trúc, đang đo qua E1.*
- **H2 → P1.** Chuyển bước có handoff file trong `stories/<KEY>/handoffs/` (V1): mục tiêu, REQ ID, quyết định đã chốt, ràng buộc, câu hỏi mở. E1: bắt buộc ở 2 mốc. ID `<KEY>-B<n>-R<nn>` truy vết sang design, testcase, bug.
- **H3 → P2.** Kiểm tra khả thi trước khi chốt BRD: `_shared/constraints.md` + spike có timebox + AI đối chiếu BRD với kiến trúc/codebase (V3).
- **H4.** Testcase sinh từ acceptance criteria, song song với dev, không sinh từ code. Mỗi testcase ghi `covers:` AC; CI kiểm độ phủ.

## Nguyên tắc (không đo riêng, áp cho mọi thử nghiệm)
- **H5.** Dev nhanh hơn mà Review/Test/UAT giữ nguyên → nút thắt dời chỗ. Đo cả chuỗi, không đo riêng Dev.
- **H6 → P1, P3.** Sửa harness trước khi đổi tool: guide (template, skill) + sensor (check tự động, review). File context cho AI tối thiểu.
- **H7.** Skill, prompt dùng chung do người chọn lọc, đo có/không trên 3 tình huống trước khi dùng. AI chỉ nháp.

## Thử nghiệm đang chạy
- **E1 — Bản tối giản** (từ 2026-09-24, 1 Story) → H1, H2.
  - Giả thuyết: 4 file bắt buộc (README Story · `requirements/B1` · `decisions.md` · `test/B1`) + handoff ở 2 mốc (BRD → Design/Dev, Dev → UAT) đủ giảm P1, chi phí duy trì chấp nhận được.
  - Tùy chọn: `design/`, `CHANGELOG.md` (bắt buộc 1 dòng khi đổi REQ/AC sau `approved`), ADR, skill. CI chế độ cảnh báo (`check_docs.py` không `--strict`).
  - Đo, baseline từ Story hiện tại → sau 1 Story: số lần hỏi lại điều đã chốt · quyết định trong chat vs trong `decisions.md` · thời gian chốt trong chat → có trong file · phút/người/ngày duy trì repo.
  - Dừng: > 15 phút/người/ngày, hoặc < 50% quyết định vào file sau 2 tuần → cắt tiếp (bỏ CHANGELOG tay, lấy từ tiêu đề PR).
  - Rủi ro: bỏ handoff Design → Review có thể làm P1 quay lại ở bước 3–4; đếm số lần quay lại bước 2.

## Ràng buộc
- [ngân sách · thời gian thử nghiệm · tool bắt buộc · compliance]
- Chính sách dữ liệu chưa rõ → chưa: đưa code, dữ liệu khách hàng lên LLM cloud; cho AI đọc repo code (V3); cân nhắc tool self-host.

## Thuật ngữ nội bộ
→ `_shared/glossary.md`
