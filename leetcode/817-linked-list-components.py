"""
@complexity
time: O(n)
space: O(1)
"""


class Solution(object):
    def numComponents(self, head, nums):
        """
        :type head: Optional[ListNode]
        :type nums: List[int]
        :rtype: int
        """

        nums_set = set(nums)
        current = head
        total = 0

        while current:
            if current.val in nums_set and (current.next is None or current.next.val not in nums_set):
                total += 1

            current = current.next

        return total
