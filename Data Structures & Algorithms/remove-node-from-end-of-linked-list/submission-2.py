# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        tam = ListNode(0, head)
        left = tam
        right = head

        while n > 0:
            right = right.next
            n -= 1
            
        while right:
            right = right.next
            left = left.next

        left.next = left.next.next 

        return tam.next