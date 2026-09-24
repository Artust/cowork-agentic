# Ví dụ AC

## Tốt
- **DEMO-1-B1-R01-AC2**: Given OTP đã gửi When quá 3 phút Then OTP hết hạn (xem DEMO-1-D02)

## Chưa tốt → sửa
- ❌ Given người dùng When đăng nhập Then hệ thống hoạt động nhanh
  - "nhanh" không đo được → ✅ Then vào màn Home trong ≤ 2 giây
- ❌ Given sai OTP 5 lần When nhập lần 6 Then khóa tài khoản và gửi email và ghi log
  - 3 hành vi → tách 3 AC
