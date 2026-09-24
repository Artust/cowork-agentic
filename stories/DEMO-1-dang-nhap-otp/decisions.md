# Quyết định — DEMO-1

Không sửa quyết định `accepted`. Đổi → thêm quyết định mới ghi `supersedes`, đổi trạng thái cũ thành `superseded by`.
Ảnh hưởng nhiều Story → `_shared/decisions/` (cùng format). Mới nhất ở trên.

## DEMO-1-D02 — OTP hết hạn sau 3 phút
- Trạng thái: accepted
- Ngày: 2026-09-22 · Người chốt: PO-Tuấn
- Supersedes: DEMO-1-D01
- Ảnh hưởng: DEMO-1-B1-R01-AC2
- Bối cảnh: Bảo mật yêu cầu rút ngắn thời gian sống của OTP. SMS giờ cao điểm có thể trễ (spike B1).
- Quyết định: 3 phút. 1 phút quá ngắn khi SMS trễ; 5 phút quá dài theo bảo mật.
- Hệ quả: sửa AC2, testcase TC02.
- Phương án đã xét: 5 phút · 3 phút · 1 phút

## DEMO-1-D01 — OTP hết hạn sau 5 phút
- Trạng thái: superseded by DEMO-1-D02
- Ngày: 2026-09-18 · Người chốt: PO-Tuấn
- Ảnh hưởng: DEMO-1-B1-R01-AC2
- Bối cảnh: chuẩn cũ của hệ thống.
- Quyết định: 5 phút, giữ theo chuẩn cũ.
- Hệ quả: —
