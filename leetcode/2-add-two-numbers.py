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
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        current = head
        hashSet = set()

        while current:
            if current in hashSet:
                return True
            hashSet.add(current)
            current = current.next

        return False
