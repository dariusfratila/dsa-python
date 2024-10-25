"""
@complexity
time: O(n)
space: O(1)
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        ahead = current = dummy

        while (n + 1):
            ahead = ahead.next
            n -= 1

        while ahead:
            ahead = ahead.next
            current = current.next

        current.next = current.next.next

        return dummy.next
