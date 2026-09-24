---
brd: DEMO-1-B1
owner: Tester-Hà
updated: 2026-09-23
---
# Testcase — DEMO-1-B1

Mỗi testcase ghi `covers:` các AC nó kiểm tra. Sinh từ AC, không từ code.

### DEMO-1-B1-TC01 — Nhận OTP với số đã đăng ký
- covers: DEMO-1-B1-R01-AC1
- Tiền điều kiện: số test đã đăng ký
- Bước: nhập số → "Gửi mã"
- Kỳ vọng: SMS 6 số trong 30s

### DEMO-1-B1-TC02 — OTP hết hạn sau 3 phút
- covers: DEMO-1-B1-R01-AC2
- Bước: gửi OTP → chờ 3 phút 5 giây → nhập OTP
- Kỳ vọng: báo hết hạn

### DEMO-1-B1-TC03 — Khóa nút gửi lại 60 giây
- covers: DEMO-1-B1-R02-AC1
- Bước: gửi OTP → bấm "Gửi lại" ngay
- Kỳ vọng: nút khóa, đếm ngược từ 60
