"""
@complexity
time: O(n)
space: O(1)
"""


class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return head

        oddPointer = head
        evenPointer = head.next
        evenHead = evenPointer

        while evenPointer and evenPointer.next:
            oddPointer.next = evenPointer.next
            oddPointer = oddPointer.next

            evenPointer.next = oddPointer.next
            evenPointer = evenPointer.next

        oddPointer.next = evenHead

        return head
