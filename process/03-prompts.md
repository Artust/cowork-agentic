# Prompt library
Thay phần `[ ]` trước khi chạy.
Vòng lặp: P1 nghiên cứu → P2 đọc sâu → thử trên 1 Story → P3 rút kinh nghiệm → ghi `04-learning-log.md` (qua PR).
Quy ước ID, đường dẫn: `README.md` repo tài liệu. REQ `<KEY>-B<n>-R<nn>` · AC `<REQ>-AC<n>` · quyết định `<KEY>-D<nn>` · ràng buộc `C-<nnn>`.

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

# B. Vận hành — thử ngay trên 1 Story

## V1 — Handoff packet (chạy khi chuyển bước) → P1

```
Input: folder stories/[KEY-slug] (README, requirements, design, decisions, CHANGELOG).
Tạo file bàn giao bước [N] → [N+1] theo templates/handoff.md.
Lưu: handoffs/[YYYY-MM-DD]-[từ]-to-[đến].md. Người nhận: [vai trò].

- Mục tiêu, 2 dòng
- Phạm vi: có / không
- REQ ID + AC liên quan: link, không chép
- Quyết định đã chốt: link <KEY>-Dxx
- Ràng buộc kỹ thuật: link C-xxx
- Thay đổi so với lần bàn giao trước: link dòng CHANGELOG
- Câu hỏi mở + người trả lời
- Rủi ro

Sau đó:
1. Liệt kê thông tin có trong input nhưng chưa vào gói. Hỏi người gửi: thêm hay bỏ.
2. Viết 5 câu hỏi kiểm tra cho người nhận. Trả lời sai → context chưa đủ, bổ sung gói.
```

## V2 — Chốt phiên (chạy cuối mỗi chat làm việc) → P3

```
Từ chat này, xuất 3 khối dán thẳng vào repo. Không có gì mới → "không thay đổi".

1. decisions.md — mỗi quyết định:
## <KEY>-Dxx — [tiêu đề]
- Trạng thái: proposed | accepted | superseded by <KEY>-Dyy
- Ngày · Người chốt
- Supersedes: [nếu có]
- Ảnh hưởng: REQ ID, file design
- Bối cảnh · Phương án đã xét · Quyết định + lý do · Hệ quả

2. CHANGELOG.md — mỗi thay đổi 1 dòng:
- <Added|Changed|Removed> <ID>: <nội dung>. Lý do: <KEY-Dxx>. Người chốt: <tên>. PR: #

3. README Story — câu hỏi mở mới (câu hỏi · người trả lời · hạn), việc đang chờ.

Thêm 1 dòng cho PR: Output AI trong phiên: dùng nguyên / sửa nhẹ / viết lại — lý do.
Quyết định ảnh hưởng ≥ 2 Story → đề xuất ADR trong _shared/decisions/.
```

## V3 — Kiểm tra khả thi trước khi chốt BRD → P2

```
Input: requirements/B[n]-….md + _shared/constraints.md + _shared/architecture.md + [codebase, nếu chính sách dữ liệu cho phép].

Với mỗi REQ ID:
- Khả thi: có / có điều kiện / không / chưa rõ
- Ràng buộc chạm phải: C-xxx hoặc đường dẫn code
- Phương án thay thế + đánh đổi
- Cần spike? Câu hỏi spike phải trả lời, timebox

Xuất:
1. Bảng theo REQ ID.
2. REQ rủi ro cao cần Dev xác nhận trước khi chuyển BRD sang approved.
3. Ràng buộc mới phát hiện → dòng đề xuất cho _shared/constraints.md.
Không chắc → ghi "chưa rõ", không đoán.
```

## V4 — Nháp skill từ phiên làm việc → H7

```
Input: chat này + bản cuối đã được người sửa + skills/README.md.
Chỉ chạy khi cùng một kiểu lỗi/sửa lặp ≥ 2 lần.

1. Liệt kê chỗ AI sai hoặc thiếu context trong phiên, kèm cách người đã sửa.
2. Bỏ những gì AI đã tự biết. Giữ quy ước riêng của team.
3. Nháp skills/[ten-skill]/SKILL.md: name, description (khi nào dùng), metadata (owner, version 0.1, status: draft, review-by, evidence: trống), thân < 500 dòng, mỗi quy tắc kèm lý do.
4. Viết 3 tình huống kiểm tra + kết quả mong đợi, để chạy có/không skill.
Không tự đánh dấu skill là đã kiểm chứng.
```
