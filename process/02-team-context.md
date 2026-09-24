# Team context — AI trong phát triển phần mềm
Cập nhật: 2026-09-20 · Người giữ file: [?]
`[?]` = chưa có thông tin, cần điền.

## Team
- Vai trò: BA, Designer, Dev, Tester, [PM/PO?]
- Quy mô: [?] người · Làm việc: [onsite / remote / hybrid]
- Sản phẩm, domain: [?]
- Loại dự án: [greenfield / brownfield / outsourcing]
- Stack: [?]
- Công cụ: issue tracker [?] · tài liệu [?] · repo [?] · design Figma · chat [?]
- AI đang dùng: [?] · Ai có license: [?]
- Chính sách dữ liệu: [được / không đưa code, dữ liệu khách hàng vào AI]

## Flow hiện tại
| # | Bước | Tham gia | Output |
|---|------|----------|--------|
| 1 | Research | BA + Dev | [?] |
| 2 | BRD | Cả team | BRD |
| 3 | Design: wireframe/Figma + design detail của Dev | Designer + BA + Dev + Test | Figma, design detail |
| 4 | Review: sai sót → quay lại 2, ổn → đi tiếp | Cả team | [?] |
| 5 | Execute: develop + viết testcase | Dev + Test | Code, testcase |
| 6 | UAT | [?] | [?] |
| 7 | Fix bug | [?] | |
| 8 | Deploy | [?] | |

## Vấn đề
- **P1 — Mất context khi chuyển bước.** Người xử lý không nắm hết hoặc quên.
- **P2 — Giới hạn công nghệ phát hiện muộn.** Phải sửa lại BRD hoặc design.
- **P3 — Thông tin phân mảnh.** Update liên tục sinh nhiều chat/thread trong workspace → sót, mất thông tin.

## Mục tiêu
- Mọi vai trò dùng AI để tăng tốc độ phát triển.
- Chỉ số muốn cải thiện: [lead time ý tưởng → deploy · số lần quay lại bước 2 · bug lọt tới UAT · giờ viết BRD, testcase]
- Baseline: [?]

## Giả thuyết đang xét (chưa kiểm chứng)
- **H1 → P3.** Nguồn sự thật = tài liệu sống có version, không phải chat. Mỗi feature một nơi chứa duy nhất gồm: BRD · design/tech spec · decision log · change log. Chat nào kết thúc cũng ghi quyết định, thay đổi về tài liệu (prompt V2).
- **H2 → P1.** Chuyển bước bắt buộc có handoff packet: mục tiêu, REQ ID, quyết định đã chốt, ràng buộc, câu hỏi mở (prompt V1). Mỗi yêu cầu trong BRD mang mã REQ-xxx để truy vết sang design, testcase, bug.
- **H3 → P2.** Kiểm tra khả thi trước khi chốt BRD: constraints register dùng chung + spike có timebox + AI đối chiếu BRD với kiến trúc/codebase (prompt V3).
- **H4.** Testcase sinh từ acceptance criteria, song song với dev, không sinh từ code.
- **H5.** Dev nhanh hơn mà Review/Test/UAT giữ nguyên → nút thắt dời chỗ. Đo cả chuỗi, không đo riêng Dev.

## Ràng buộc
- [ngân sách · thời gian thử nghiệm · tool bắt buộc · compliance]

## Thuật ngữ nội bộ
- [?]
