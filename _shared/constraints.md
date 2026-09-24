# Constraints register

Ràng buộc kỹ thuật, pháp lý, hạ tầng áp cho nhiều Story. V3 đối chiếu BRD với file này.
Mỗi ràng buộc 1 dòng. Hết hiệu lực → đổi trạng thái, không xóa.

| ID | Ràng buộc | Loại | Nguồn | Áp cho | Owner | Xác minh | Trạng thái |
|---|---|---|---|---|---|---|---|
| C-001 | (Ví dụ — xóa) SMS gateway giới hạn 1 tin/số/60s | Tích hợp | Hợp đồng nhà mạng; `code: services/sms/client.ts` | Mọi luồng gửi SMS | Dev-Minh | 2026-09-20 | active |

Loại: Hạ tầng · Bảo mật · Pháp lý · Hiệu năng · Tích hợp · Dữ liệu.
Trạng thái: active · retired.
