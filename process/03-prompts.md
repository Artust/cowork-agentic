# Prompt library
Thay phần `[ ]` trước khi chạy.
Vòng lặp: P1 nghiên cứu → P2 đọc sâu → thử trên 1 feature → P3 rút kinh nghiệm → ghi `04-learning-log.md`.

---

# A. Nghiên cứu

## P1 — Deep research
Bật Research nếu có.

```
Chủ đề: [vd: spec-driven development cho team có BA, Dev, Tester]
Bối cảnh: đọc 02-team-context.md. Bắt đầu từ nguồn trong 04-learning-log.md, rồi mở rộng.

Câu hỏi:
1. Phương pháp, mô hình nào đang được dùng thật? Ai dùng, quy mô, loại dự án?
2. Vận hành cụ thể: vai trò, artifact, nghi thức, tool, điểm người kiểm soát.
3. Kết quả đo được: số liệu, cách đo, thời gian theo dõi. Tách số đo thật với tự báo cáo.
4. Thất bại, chi phí ẩn, điều kiện tiên quyết.
5. Phần nào khớp flow 8 bước của team? Giải quyết P1/P2/P3 thế nào?

Quy tắc nguồn:
- ≥ 15 nguồn, ưu tiên 12 tháng gần nhất, ghi ngày.
- Gắn nhãn A/B/C/D. Tối thiểu 3 nguồn A hoặc B; không đủ → nói rõ.
- Chủ động tìm ý kiến phản biện cho từng phương pháp.
- Đọc nguồn gốc, không dừng ở bài tóm tắt.

Output:
1. Tóm tắt 5 dòng.
2. Bảng: phương pháp · cách vận hành · bằng chứng (nhãn) · giới hạn · khớp bước · giải quyết P nào.
3. 2–3 case study: bối cảnh → làm gì → kết quả → vì sao áp dụng được / không được cho team.
4. Sơ đồ flow của team sau khi áp dụng phương án khả thi nhất.
5. 3 thử nghiệm: giả thuyết · phạm vi 1 feature · cách đo · tiêu chí dừng.
6. Điều chưa biết + câu hỏi team cần trả lời.
7. LEARNING LOG.
```

## P2 — Deep read (1 nguồn)

```
Nguồn: [URL hoặc file đính kèm]

1. Luận điểm chính, 3 dòng.
2. Mô hình vận hành: ai làm gì, artifact nào, thứ tự, tool.
3. Bằng chứng: số liệu, cỡ mẫu, cách đo, ai tài trợ. Nhãn A/B/C/D.
4. Điều kiện để kết quả đúng. Khác bối cảnh team ở đâu?
5. Điểm yếu, thiên lệch của nguồn.
6. Áp dụng: bước nào trong flow, P nào, việc nhỏ nhất thử được tuần này.
7. So với learning log: xác nhận / mâu thuẫn / mới.
8. LEARNING LOG.
```

## P3 — Rút kinh nghiệm sau thử nghiệm

```
Input: giả thuyết ban đầu, số đo trước/sau, ghi chú của BA, Dev, Tester [đính kèm].

1. Kỳ vọng vs thực tế, theo từng chỉ số.
2. Cái gì hiệu quả, vì sao. Cái gì không, vì sao. Tách nguyên nhân: tool / quy trình / kỹ năng / bối cảnh.
3. Khác gì so với nguồn đã đọc trong log?
4. Quyết định: giữ / sửa / bỏ. Thay đổi cụ thể cho vòng sau.
5. Đề xuất sửa mục Giả thuyết trong 02-team-context.md.
6. LEARNING LOG.
```

---

# B. Vận hành — thử ngay trên 1 feature

## V1 — Handoff packet (chạy khi chuyển bước) → P1

```
Input: tài liệu hiện hành của bước [N] + decision log.
Tạo gói bàn giao cho bước [N+1]. Người nhận: [vai trò].

- Mục tiêu feature, 2 dòng
- Phạm vi: có / không
- Yêu cầu theo REQ ID + acceptance criteria
- Quyết định đã chốt + lý do, ngày, người chốt
- Ràng buộc kỹ thuật
- Thay đổi so với bản trước
- Câu hỏi mở + người trả lời
- Rủi ro

Sau đó:
1. Liệt kê thông tin có trong input nhưng chưa vào gói. Hỏi người gửi: thêm hay bỏ.
2. Viết 5 câu hỏi kiểm tra cho người nhận. Trả lời sai → context chưa đủ, bổ sung gói.
```

## V2 — Chốt phiên (chạy cuối mỗi chat làm việc) → P3

```
Từ chat này, xuất:
- Quyết định mới: nội dung · lý do · người chốt · REQ, design bị ảnh hưởng
- Thay đổi cần ghi vào BRD / design / testcase: vị trí + nội dung mới
- Câu hỏi mở + người phụ trách
- Thứ bị thay thế, hủy

Định dạng dán thẳng vào decision log và change log.
Không có gì mới → ghi "không thay đổi".
```

## V3 — Kiểm tra khả thi trước khi chốt BRD → P2

```
Input: BRD nháp + constraints register + [mô tả kiến trúc hoặc codebase].

Với mỗi REQ:
- Khả thi: có / có điều kiện / không / chưa rõ
- Ràng buộc chạm phải (trích constraints register hoặc code)
- Phương án thay thế + đánh đổi
- Cần spike? Câu hỏi spike phải trả lời, timebox

Xuất: bảng theo REQ ID + danh sách REQ rủi ro cao cần Dev xác nhận trước khi ký BRD.
Không chắc → ghi "chưa rõ", không đoán.
```
