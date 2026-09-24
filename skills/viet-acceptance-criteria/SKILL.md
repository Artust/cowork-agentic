---
name: viet-acceptance-criteria
description: Viết acceptance criteria Given/When/Then cho yêu cầu trong BRD theo quy ước ID của repo tài liệu. Dùng khi BA nháp hoặc sửa yêu cầu trong stories/*/requirements/, hoặc khi Tester cần AC rõ để sinh testcase.
metadata:
  owner: "[?]"
  version: "0.1"
  status: "draft — chưa qua 3 tình huống kiểm tra"
  review-by: "[?]"
  evidence: "[?]"
---
# Viết acceptance criteria

## Định dạng
Mỗi AC là 1 dòng list ngay dưới heading yêu cầu:
`- **<REQ>-AC<n>**: Given <trạng thái> When <hành động> Then <kết quả quan sát được>`
Lý do: `scripts/check_docs.py` và Tester dựa vào đúng định dạng này để truy vết AC → testcase.

## Quy tắc
- Then phải quan sát/đo được (số, thời gian, thông báo cụ thể). "Hoạt động tốt" không kiểm tra được.
- 1 AC = 1 hành vi. Nhiều "and" trong Then → tách AC. Lý do: testcase map 1-1 dễ truy lỗi.
- Có con số → dẫn nguồn quyết định (`<KEY>-Dxx`) hoặc ràng buộc (`C-xxx`). Lý do: con số hay đổi, cần biết ai chốt.
- Thiếu thông tin → ghi "chưa rõ" và thêm vào "Câu hỏi mở" trong README Story. Không tự điền giá trị.
- Không đổi ID đã có. AC bỏ → ghi `Removed` trong CHANGELOG, không tái dùng ID.

## Ví dụ
`references/vi-du.md`
