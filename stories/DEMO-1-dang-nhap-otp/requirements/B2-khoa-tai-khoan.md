---
id: DEMO-1-B2
title: Khóa tài khoản khi nhập sai
status: approved     # draft | review | approved
owner: BA-An
tasks: [DEMO-13]
updated: 2026-09-22
---
# DEMO-1-B2 — Khóa tài khoản khi nhập sai

## Mục tiêu
Chặn dò OTP.

## Phạm vi
- Có: đếm số lần sai, khóa tạm.
- Không: cách mở khóa (câu hỏi mở #1 trong README).

## Yêu cầu

### DEMO-1-B2-R01 — Khóa sau 5 lần sai
- **DEMO-1-B2-R01-AC1**: Given nhập sai OTP 4 lần When nhập sai lần 5 Then tài khoản bị khóa, hiện thông báo
- **DEMO-1-B2-R01-AC2**: Given tài khoản bị khóa When yêu cầu OTP mới Then không gửi OTP
- Ràng buộc: không

## Giả định
- Đếm theo tài khoản, không theo thiết bị.
