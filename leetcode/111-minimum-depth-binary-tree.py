"""
@complexity
time: O(n)
space: O(h)
"""


class Solution(object):
    def minDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        if not root:
            return 0

        def dfs(node, depth):
            if not node:
                return float('inf')

            if not node.left and not node.right:
                return depth

            return min(dfs(node.left, depth + 1), dfs(node.right, depth + 1))

        return dfs(root, 1)
