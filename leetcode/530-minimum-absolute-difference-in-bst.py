"""
@complexity
time: O(n)
space: O(n)
"""


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        min_difference = float('inf')
        prev = None

        def dfs(node):
            nonlocal min_difference, prev
            if not node:
                return

            dfs(node.left)

            if prev is not None:
                min_difference = min(min_difference, abs(node.val - prev))
            prev = node.val

            dfs(node.right)

        dfs(root)
        return min_difference
