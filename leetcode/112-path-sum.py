"""
@complexity
time: O(n)
space: O(h)
"""


class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """

        def dfs(node, sum_reached):
            if not node:
                return False

            sum_reached += node.val
            if not node.left and not node.right:
                return sum_reached == targetSum

            left_tree = dfs(node.left, sum_reached)
            right_tree = dfs(node.right, sum_reached)
            return left_tree or right_tree

        if not root:
            return False

        return dfs(root, 0)
