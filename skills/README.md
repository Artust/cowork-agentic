# Skills

Chuẩn: [agentskills.io](https://agentskills.io). 1 skill = 1 folder chứa `SKILL.md` (+ `references/`, `scripts/`, `assets/` nếu cần).
Người chọn lọc, AI chỉ viết nháp: skill AI tự sinh chưa qua kiểm tra thường làm kết quả kém đi (SkillsBench, 2026).

## Tạo skill
1. Cho AI làm việc thật KHÔNG có skill. Ghi chỗ sai, thiếu context.
2. Dựng 3 tình huống kiểm tra đúng các chỗ đó. Ghi kết quả không skill (baseline).
3. Viết hướng dẫn tối thiểu đủ qua 3 tình huống. Mỗi quy tắc kèm lý do.
4. Chạy lại 3 tình huống với skill, so baseline. Không tốt hơn → không merge.
5. Ghi kết quả vào `metadata.evidence`.

Giới hạn: `name` ≤ 64 ký tự (chữ thường, số, gạch ngang) · `description` ≤ 1.024 ký tự, nói rõ khi nào dùng · thân < 500 dòng · file tham chiếu cách `SKILL.md` 1 cấp.

## Checklist review (PR vào skills/)
**An toàn** — Dev
- [ ] Đọc hết `scripts/`, không chỉ `SKILL.md`
- [ ] Không lệnh xóa, gửi dữ liệu ra ngoài, link lạ, chỉ thị ẩn
- [ ] Skill từ nguồn ngoài: đã đọc toàn bộ trước khi đưa vào

**Kích hoạt** — owner
- [ ] 3 prompt lẽ ra phải dùng skill → AI dùng
- [ ] 2 prompt không liên quan → AI không dùng

**Chất lượng viết** — 1 người dùng skill thuộc vai trò khác
- [ ] Không lặp kiến thức AI đã biết
- [ ] Quy tắc có lý do, không chỉ ALWAYS/NEVER/MUST
- [ ] Không thông tin sẽ lỗi thời theo ngày tháng
- [ ] Không trùng skill khác

**Hiệu quả** — owner
- [ ] Kết quả 3 tình huống có skill tốt hơn baseline, ghi trong `metadata.evidence`

**Vòng đời** — owner
- [ ] Có `review-by`. Đến hạn: xét lại; không còn cải thiện → xóa
