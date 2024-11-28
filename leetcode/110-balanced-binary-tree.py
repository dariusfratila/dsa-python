"""
@complexity
time: O(n)
space: O(h)
"""


class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def check_balance_and_get_depth(node):
            if not node:
                return 0

            left_depth = check_balance_and_get_depth(node.left)
            right_depth = check_balance_and_get_depth(node.right)

            if left_depth == -1 or right_depth == -1 or abs(left_depth - right_depth) > 1:
                return -1

            return max(left_depth, right_depth) + 1

        return check_balance_and_get_depth(root) != -1
