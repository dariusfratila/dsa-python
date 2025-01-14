"""
@complexity
time: O(n)
space: O(n)
"""


class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        result = 0

        a_set = set()
        b_set = set()
        c_set = []

        for index in range(len(A)):
            if A[index] in b_set:
                result += 1
            a_set.add(A[index])

            if B[index] in a_set:
                result += 1
            b_set.add(B[index])

            c_set.append(result)

        return c_set
