"""
@complexity
time: O(n)
space: O(1)
"""


class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """

        dummy = ListNode(0)
        dummy.next = head

        current = dummy
        while current and current.next:
            while current.next and current.next.val == val:
                current.next = current.next.next
            current = current.next

        return dummy.next
