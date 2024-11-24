"""
@complexity
time: O(n^2)
space: O(1)
"""


class Solution(object):
    def insertionSortList(self, head):
        dummy = ListNode(0, head)
        prev, current = head, head.next

        while current:
            if current.val >= prev.val:
                prev, current = current, current.next
                continue

            temp = dummy
            while current.val > temp.next.val:
                temp = temp.next

            prev.next = current.next
            current.next = temp.next
            temp.next = current
            current = prev.next

        return dummy.next
