"""
@complexity
time: O(n)
space: O(1)
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        dummy = ListNode(0, head)
        prev, curr = dummy, head

        while curr and curr.next:
            next_pair = curr.next.next
            second_element = curr.next

            second_element.next = curr
            curr.next = next_pair
            prev.next = second_element

            prev = curr
            curr = next_pair

        return dummy.next
