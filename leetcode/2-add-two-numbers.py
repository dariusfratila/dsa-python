"""
@complexity
time: O(n)
space: O(n)
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy

        carry = 0
        while l1 or l2:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            sumElements = val1 + val2 + carry

            carry = sumElements // 10
            sumElements %= 10

            current.next = ListNode(sumElements)
            current = current.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        if carry:
            current.next = ListNode(carry)

        return dummy.next
