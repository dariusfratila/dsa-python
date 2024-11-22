"""
@complexity
time: O(n)
space: O(1)
"""


class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """

        res = 0
        while head:
            res = (res << 1) | head.val
            head = head.next

        return res
