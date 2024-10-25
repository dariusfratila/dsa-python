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
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find middle
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        print(slow.val)
        # invert elements from second half
        prev, current = None, slow.nexts
        while current:
            tmp = current.next
            print(f'tmp:{tmp}')
            print(f'current.next:{prev}')
            current.next = prev
            prev = current
            current = tmp

        slow.next = None

        head1, head2 = head, prev
        while head2:
            tmp1, tmp2 = head1.next, head2.next
            head1.next = head2
            head2.next = tmp1
            head1, head2 = tmp1, tmp2
        # merge lists
