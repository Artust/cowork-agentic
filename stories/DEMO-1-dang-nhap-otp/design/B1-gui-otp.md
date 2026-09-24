---
brd: DEMO-1-B1
owner: Designer-Linh
figma: [link frame kèm node-id]
figma_version: [tên/ngày version]
updated: 2026-09-22
---
# Design — DEMO-1-B1

## Màn hình / luồng
| REQ | Frame Figma | Ghi chú |
|---|---|---|
| DEMO-1-B1-R01 | Login / Nhập số | |
| DEMO-1-B1-R02 | Login / Nhập OTP | Đếm ngược 60s trên nút "Gửi lại" |

## Tech detail
- API / contract: `POST /auth/otp` → 202; `POST /auth/otp/verify`
- Dữ liệu: bảng `otp_requests` (phone_hash, code_hash, expires_at, attempts)
- Thay đổi ở repo code: `services/auth/otp.ts`, `services/sms/client.ts`

## Ràng buộc chạm phải
- C-001: gateway 1 tin/số/60s → khóa nút gửi lại 60s (DEMO-1-B1-R02-AC1)

## Rủi ro / cần spike
- Độ trễ SMS giờ cao điểm có vượt 30s? Spike 0,5 ngày, Dev-Minh.
