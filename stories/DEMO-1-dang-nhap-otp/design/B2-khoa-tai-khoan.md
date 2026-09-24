---
brd: DEMO-1-B2
owner: Dev-Minh
figma: [link frame kèm node-id]
figma_version: [tên/ngày version]
updated: 2026-09-22
---
# Design — DEMO-1-B2

## Màn hình / luồng
| REQ | Frame Figma | Ghi chú |
|---|---|---|
| DEMO-1-B2-R01 | Login / Tài khoản bị khóa | |

## Tech detail
- Dữ liệu: thêm `locked_until` vào `users`
- Thay đổi ở repo code: `services/auth/otp.ts`

## Ràng buộc chạm phải
- Không

## Rủi ro / cần spike
- Chờ câu hỏi mở #1 (cách mở khóa).
