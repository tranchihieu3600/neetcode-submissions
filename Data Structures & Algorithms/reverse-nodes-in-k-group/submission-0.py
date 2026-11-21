# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k <= 1:
            return head

        dummy = ListNode(0, head)
        group_prev = dummy  # Luôn đứng ngay trước nhóm k node hiện tại

        while True:
            # Bước 1: Tìm node thứ k tính từ group_prev
            kth = group_prev
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next  # Không đủ k node -> giữ nguyên phần còn lại

            group_next = kth.next  # Node đầu tiên của phần sau nhóm này

            # Bước 2: Đảo ngược k node trong nhóm (từ group_prev.next tới kth)
            prev = group_next
            curr = group_prev.next
            while curr != group_next:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            # Bước 3: Nối lại vào danh sách chính và dời group_prev về đuôi mới của nhóm
            old_group_head = group_prev.next  # Sau khi đảo, node này thành đuôi mới
            group_prev.next = kth             # Nối node đứng trước nhóm tới đầu mới (kth)
            group_prev = old_group_head       # Cập nhật group_prev cho nhóm kế tiếp