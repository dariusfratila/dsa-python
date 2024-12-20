"""
@complexity
time: O(n)
space: O(h)
"""


class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack = []

        current = root
        sum_value = 0

        while stack or current:
            while current:
                stack.append(current)
                current = current.right

            node = stack.pop()
            sum_value += node.val
            node.val = sum_value

            current = node.left

        return root
