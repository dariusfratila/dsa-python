"""
@complexity
time: O(n)
space: O(n)
"""


class Solution:
    def isValid(self, s: str) -> bool:
        Map = {")": "(", "]": "[", "}": "{"}
        stack = []

        for element in s:
            if element not in Map:
                # print(element)
                stack.append(element)
            else:
                if stack and stack[-1] == Map[element]:
                    stack.pop()
                else:
                    return False

        return not stack
