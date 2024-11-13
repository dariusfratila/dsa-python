"""
@complexity
time: O(n + m)
space: O(1)
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """

        list1, list2 = headA, headB

        count_list1, count_list2 = 0, 0
        while list1:
            count_list1 += 1
            list1 = list1.next

        while list2:
            count_list2 += 1
            list2 = list2.next

        listLonger, listShorter = 0, 0
        difference = 0
        if count_list1 > count_list2:
            listLonger = headA
            difference = count_list1 - count_list2
            listShorter = headB
        else:
            listLonger = headB
            difference = count_list2 - count_list1
            listShorter = headA

        while difference:
            listLonger = listLonger.next
            difference -= 1

        while listLonger != listShorter:
            listLonger = listLonger.next
            listShorter = listShorter.next

        return listLonger
