# Learning log
Mới nhất ở trên. Nhãn: [A] đo trực tiếp · [B] khảo sát lớn · [C] practitioner, case study · [D] vendor marketing.

---

## 2026-09-23 — Hermes Agent, harness, skill, cấu trúc tài liệu
Câu hỏi: Hermes là gì, bài học gì? Harness/skill đo thế nào? Source of truth lưu ra sao?

### Phát hiện
1. **Harness quan trọng ngang model; context file càng ít càng tốt.**
   - [A] Claw-SWE-Bench (06/2026): giữ model, đổi harness → Pass@1 chênh 12.5–27.4 điểm. Hermes Agent 71.1%, thứ 2 sau OpenClaw, đắt hơn. 1 lần chạy; memory/skill của Hermes bị tắt. https://arxiv.org/abs/2606.12344
   - [A] ETH Zurich, "Evaluating AGENTS.md" (02/2026): context file có xu hướng giảm tỷ lệ thành công, tăng chi phí > 20%. Khuyến nghị: chỉ ghi yêu cầu tối thiểu, thứ AI không tự suy ra được. Nghiên cứu ngược (Lulla et al.) thấy nhanh hơn, ít token hơn, mẫu nhỏ. https://arxiv.org/abs/2602.11988
   - [C] Böckeler, "Harness engineering" (04/2026): harness = guide (trước) + sensor (sau), tất định hoặc suy luận. Chưa có cách đo độ phủ harness. https://martinfowler.com/articles/harness-engineering.html
   - → Bổ sung mục 8 (log 2026-09-20): instructions chung phải ngắn, người viết.
2. **Skill: người chọn lọc, đo có/không; AI chỉ nháp.**
   - [A, chưa peer-review] SkillsBench (02/2026), 86 task, 7.308 trajectory: skill chọn lọc +16.2 điểm trung bình; Software Engineering chỉ +4.5; 16/84 task kém đi; skill tự sinh không lợi trung bình; skill gọn 2–3 module tốt hơn tài liệu đầy đủ. Skill tự sinh ở đây viết TRƯỚC khi làm task, khác Hermes (sau trải nghiệm). https://arxiv.org/abs/2602.12670
     - Đính chính: số nêu trong chat trước (+16.6; tự sinh −8.1 đến −11.5) lấy từ nguồn thứ cấp. Dùng số abstract ở trên.
   - [C] Quy trình eval-first: chạy không skill → ghi lỗi → 3 tình huống → baseline → viết tối thiểu → so. https://arxiv.org/abs/2607.25032 · Đo cặp có/không trong CI: https://arxiv.org/abs/2608.20614
3. **Skill, file context là kênh tấn công.**
   - [C] Snyk ToxicSkills (02/2026): 3.984 skill công khai, 36.82% có ít nhất 1 lỗi bảo mật, 13.4% critical. https://snyk.io/de/blog/toxicskills-malicious-ai-agent-skills-clawhub/ (bài tiếng Anh)
   - [C] CSA (05/2026): SKILL.md, CLAUDE.md, AGENTS.md là kênh đầu độc chính; file cấu hình trong repo (hook `.claude/settings.json`) từng gây chạy lệnh tùy ý ở Claude Code, đã vá. https://labs.cloudsecurityalliance.org/research/csa-research-note-skill-md-agent-context-poisoning-20260506
   - [C] Hermes Agent: audit độc lập 4 Critical / 9 High ở cấu hình mặc định (shell không giới hạn). https://github.com/NousResearch/hermes-agent/issues/7826
   - → Review skill, AGENTS.md, CLAUDE.md, `.claude/` như code.
4. **Hermes Agent (Nous Research, MIT, 02/2026): memory + skill tích lũy qua phiên.**
   - [C] "Self-improving" thực chất = skill tự tạo + pipeline RL cần người bấm; agent là nguồn dữ liệu huấn luyện cho model Hermes. https://saulius.io/blog/hermes-agent-self-improving-ai-architecture
   - [C] Memory bền vững = rủi ro quản trị mới. https://www.catonetworks.com/blog/cato-ctrl-governing-hermes-agent/
   - [D] Vendor: "được công ty lớn tin dùng", không tên, không số. https://hermes-agent.nousresearch.com/
   - Không tìm thấy nghiên cứu độc lập về năng suất team.
   - → Memory agent ≠ source of truth (H1). Không thử Hermes trừ khi chính sách dữ liệu bắt buộc self-host.
5. **Cấu trúc tài liệu cho AI.**
   - [C] BMAD: story = gói context, trích dẫn ngược về PRD/architecture; mỗi phần có người được sửa; story đã xong là hồ sơ bất biến. https://github.com/bmad-code-org/BMAD-METHOD/issues/1930
   - [C] MADR: quyết định không sửa, tạo bản mới, bản cũ "superseded". https://github.com/adr/madr
   - [C] spec-kit: folder mỗi feature + constitution chung. https://github.com/github/spec-kit
   - Công cụ: Claude Code chưa đọc được Project knowledge (feature request mở 08/2026) https://github.com/anthropics/claude-code/issues/87528 · Project đọc repo qua GitHub integration, Sync bấm tay https://support.claude.com/en/articles/10167454
   - → Team chọn: repo tài liệu riêng trên GitHub, mỗi Story 1 folder, 1 Story nhiều BRD.

### Cần thử
- Repo tài liệu trên 1 Story. Đo: số lần hỏi lại thông tin đã chốt; quyết định có trong file vs chỉ trong chat. Dừng: duy trì > 15 phút/người/ngày.
- Baseline output AI qua PR template: nguyên / sửa nhẹ / viết lại.
- Skill `viet-acceptance-criteria` theo eval-first: 3 tình huống có/không.

### Câu hỏi mở
- Chính sách dữ liệu: được đưa code, dữ liệu lên LLM cloud? AI được đọc repo code cho V3?
- Baseline: lead time, số lần quay lại bước 2, bug lọt UAT.
- Bằng chứng cho AI ở tài liệu BA, Tester (không phải code)? Chưa tìm thấy.
- Skill rút sau trải nghiệm (kiểu Hermes) có giúp không? SkillEvolBench chưa đọc.

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
