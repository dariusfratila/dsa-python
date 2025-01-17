"""
@complexity
time: O(n)
space: O(1)
"""

import random

class Solution(object):

    def __init__(self, head):
        """
        :type head: Optional[ListNode]
        """

        self.head = head

    def getRandom(self):
        """
        :rtype: int
        """

        result = None
        count = 0.0
        current = self.head

        while current:
            count += 1
            rd = random.random()
            if rd < (1 / count):
                result = current.val
            current = current.next

        return result
