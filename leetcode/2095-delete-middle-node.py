"""
@complexity
time: O(n)
space: O(1)
"""


class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        dummy = ListNode(0)
        dummy.next = head

        prev = dummy
        slow, fast = head, head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        prev.next = slow.next

        return dummy.next
