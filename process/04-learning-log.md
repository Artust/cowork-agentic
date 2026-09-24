# Learning log
Mới nhất ở trên. Nhãn: [A] đo trực tiếp · [B] khảo sát lớn · [C] practitioner, case study · [D] vendor marketing.

---

## 2026-09-20 — Khảo sát ban đầu: AI trong SDLC cho team nhiều vai trò
Câu hỏi: phương pháp nào có thực nghiệm, khớp P1/P2/P3?

### Phát hiện
1. **[B] DORA 2025**, ~5.000 người. AI khuếch đại hiện trạng team. Lợi ích đến từ workflow rõ, nền tảng nội bộ tốt, team đồng bộ; không từ tool. 1 trong 7 năng lực: AI truy cập được tài liệu, codebase nội bộ (context engineering). → P1, P3.
   - https://dora.dev/dora-report-2025/
   - https://dora.dev/research/ai/ai-capabilities-model
   - ROI report 05/2026: https://www.infoq.com/news/2026/05/dora-roi-ai-assisted-dev-report/
2. **[B, vendor] Atlassian DevEx 2025**, 3.500 người. 68% tiết kiệm >10h/tuần nhờ AI; 50% mất >10h/tuần vì kém hiệu quả tổ chức. Tốn thời gian nhất: tìm thông tin. Code chỉ chiếm ~16% thời gian dev. → P3.
   - https://www.atlassian.com/blog/developer/developer-experience-report-2025
3. **[A, vendor] Faros AI**, telemetry >10.000 dev, 1.255 team. +21% task, +98% PR merged; review +91%, PR to hơn 154%, bug +9%. Chỉ số cấp công ty không đổi. → nút thắt dời xuống review, test.
   - https://www.faros.ai/blog/ai-software-engineering
   - Phân tích học thuật: https://arxiv.org/pdf/2605.01160
4. **[A] METR RCT.** Dev kinh nghiệm chậm hơn 19% khi dùng AI (đầu 2025), tự tin là nhanh hơn 20%. Update 02/2026: nhiều khả năng đã nhanh hơn, dữ liệu yếu. → đo, không tin cảm giác.
   - https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/
   - https://metr.org/blog/2026-02-24-uplift-update/
5. **[C] Spec-driven development** (Böckeler, martinfowler.com). 3 mức: spec-first / spec-anchored / spec-as-source. Tool hiện tại: quá tải review, cảm giác kiểm soát giả, quá nặng với việc nhỏ. → thử mức spec-anchored, nhẹ.
   - https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html
6. **[C] BMAD Method.** Agent theo vai trò (Analyst, PM, Architect, SM, Dev, QA). Story file = gói bàn giao đủ context; mỗi story một chat mới. → P1.
   - Repo gốc: tìm "BMAD-METHOD" trên GitHub
   - Hướng dẫn (vendor): https://www.augmentcode.com/guides/bmad-method-ai-development
7. **[C/D] AWS AI-DLC.** Mob Elaboration: product + eng + QA cùng phòng duyệt yêu cầu do AI nháp. Artifact, quyết định lưu trong repo. Kết quả tốt nhất ở greenfield, yêu cầu rõ, team tham gia liên tục. → P2.
   - https://awslabs.github.io/aidlc-workflows/guide/00-introduction/
8. **[C] Thoughtworks Technology Radar.** Từng người tự viết prompt từ đầu = anti-pattern. Dùng bộ instructions chung, có người chăm; việc không phải code → thư viện prompt chung. → mọi vai trò.
   - https://www.thoughtworks.com/en-us/radar/techniques/curated-shared-instructions-for-software-teams
   - https://www.thoughtworks.com/radar
9. **[C] Anthropic.** Giữ context cho việc dài hơi: compaction + ghi chú có cấu trúc ngoài context window. Cách các team nội bộ dùng Claude Code.
   - "Effective context engineering for AI agents" (Anthropic Engineering, 09/2025)
   - https://claude.com/blog/how-anthropic-teams-use-claude-code
10. **[D] BA, Tester.** Nguồn chủ yếu là vendor. Điểm chung: acceptance criteria mơ hồ → testcase sinh ra mơ hồ.

### Cần thử
H1–H5 trong `02-team-context.md`. Bắt đầu: V2 (chốt phiên) + V1 (handoff packet) trên 1 feature.

### Câu hỏi mở
- Baseline của team: lead time, số lần quay lại bước 2, bug lọt tới UAT?
- Bằng chứng độc lập cho AI ở mảng BA, Tester?
- BMAD, AI-DLC có case brownfield, team 5–15 người?
