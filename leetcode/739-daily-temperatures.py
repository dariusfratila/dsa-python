"""
@complexity
time: O(n)
space: O(n)
"""


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * (len(temperatures))
        stack = []

        for i, t in enumerate(temperatures):
            print(i, t)
            while stack and t > stack[-1][0]:
                print(stack[-1][0], stack[-1][0])
                stackValue, stackIndex = stack.pop()
                res[stackIndex] = (i - stackIndex)
            stack.append([t, i])

        return res
