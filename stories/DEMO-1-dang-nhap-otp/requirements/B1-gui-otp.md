---
id: DEMO-1-B1
title: Gửi OTP
status: approved     # draft | review | approved
owner: BA-An
tasks: [DEMO-11, DEMO-12]
updated: 2026-09-22
---
# DEMO-1-B1 — Gửi OTP

## Mục tiêu
Gửi OTP qua SMS để người dùng xác thực số điện thoại khi đăng nhập.

## Phạm vi
- Có: gửi OTP, gửi lại OTP.
- Không: OTP qua email, OTP qua app (Story khác).

## Yêu cầu

### DEMO-1-B1-R01 — Gửi OTP khi nhập số điện thoại hợp lệ
- **DEMO-1-B1-R01-AC1**: Given số điện thoại đã đăng ký When bấm "Gửi mã" Then nhận SMS chứa OTP 6 số trong 30 giây
- **DEMO-1-B1-R01-AC2**: Given OTP đã gửi When quá 3 phút Then OTP hết hạn (xem DEMO-1-D02)
- Ràng buộc: C-001

### DEMO-1-B1-R02 — Giới hạn gửi lại
- **DEMO-1-B1-R02-AC1**: Given vừa gửi OTP When bấm "Gửi lại" trước 60 giây Then nút bị khóa, hiện đếm ngược
- Ràng buộc: C-001

## Giả định
- Số điện thoại đã xác minh lúc đăng ký.
