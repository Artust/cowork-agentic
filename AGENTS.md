# AGENTS.md

Repo tài liệu. Code: `[URL repo code]`. Quy ước đầy đủ: `README.md`.

## Bản đồ
- `stories/<KEY>-<slug>/` — 1 Story. Đọc `README.md` trước.
- `_shared/` — nguyên tắc, ràng buộc, kiến trúc, glossary, ADR.
- `process/03-prompts.md` — prompt V1 (handoff), V2 (chốt phiên), V3 (khả thi).

## ID
REQ `KEY-B1-R01` · AC `KEY-B1-R01-AC1` · TC `KEY-B1-TC01` · quyết định `KEY-D01` · ADR `ADR-0001` · ràng buộc `C-001`.

## Quy tắc
- Chỉ đề xuất thay đổi qua PR.
- Không sửa Story `done`/`cancelled`.
- Không sửa quyết định `accepted`; thêm quyết định mới, ghi `supersedes`.
- `CHANGELOG.md` chỉ thêm dòng.
- Không đoán. Thiếu thông tin → ghi "chưa rõ", thêm vào "Câu hỏi mở" trong README Story.
- Dẫn nguồn bằng đường dẫn: `_shared/constraints.md#C-001`, `requirements/B1-gui-otp.md#…`.
- Chạy `python scripts/check_docs.py` trước khi đề xuất PR.
