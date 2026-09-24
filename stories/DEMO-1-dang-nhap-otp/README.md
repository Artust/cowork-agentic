---
key: DEMO-1
title: Đăng nhập bằng OTP
status: in-dev       # draft | review | ready | in-dev | uat | done | cancelled
owner: BA-An
epic: DEMO-EPIC-1
tracker: [link]
code_prs: []         # link PR repo code
updated: 2026-09-24
---
# DEMO-1 — Đăng nhập bằng OTP

> Story ví dụ. Xóa khi dùng thật.

## Mục tiêu
Người dùng đăng nhập bằng số điện thoại + OTP, không cần mật khẩu.
Giảm ticket "quên mật khẩu".

## BRD / phần
| BRD | Phạm vi | Task tracker | Owner | Trạng thái |
|---|---|---|---|---|
| [DEMO-1-B1](requirements/B1-gui-otp.md) | Gửi OTP | DEMO-11, DEMO-12 | BA-An | approved |
| [DEMO-1-B2](requirements/B2-khoa-tai-khoan.md) | Khóa tài khoản khi nhập sai | DEMO-13 | BA-An | approved |

## Đang chờ
| Việc | Ai | Hạn |
|---|---|---|
| Viết testcase DEMO-1-B2-R01-AC2 | Tester-Hà | 2026-09-26 |

## Câu hỏi mở
| # | Câu hỏi | Người trả lời | Hạn | Trạng thái |
|---|---|---|---|---|
| 1 | Mở khóa tài khoản: tự động sau 30 phút hay qua CSKH? | PO-Tuấn | 2026-09-25 | open |

## Liên quan
- Ràng buộc: `_shared/constraints.md#C-001`
- ADR: 
- Story liên quan: 
