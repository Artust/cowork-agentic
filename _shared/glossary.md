# Glossary

| Thuật ngữ | Nghĩa trong team | Không nhầm với |
|---|---|---|
| Story | Đơn vị làm việc, 1 folder trong `stories/`, có thể nhiều BRD | Task |
| BRD | Tài liệu yêu cầu cho 1 phần của Story, ID `<KEY>-B<n>` | |
| Harness | Mọi thứ quanh model quyết định AI làm tốt hay không: template, skill, file context, check tự động, review | Tool, model |
| Guide / Sensor | Guide: định hướng trước khi AI làm (template, skill). Sensor: kiểm tra sau (check_docs.py, review) | |
| Skill | Folder `skills/<ten>/SKILL.md`: cách làm một việc cụ thể, AI nạp khi cần | Prompt dùng một lần |
| Handoff | File bàn giao khi chuyển bước, trong `stories/<KEY>/handoffs/` | Tin nhắn chat |
| Source of truth | Repo này. Chat, memory của AI chỉ là nháp | |
| E1 | Thử nghiệm "bản tối giản": 4 file + 2 handoff bắt buộc, đo trên 1 Story | |
