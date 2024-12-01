"""
@complexity
time: O(log(n)^2)
space: O(log(n))
"""


class Solution(object):
    def countNodes(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        if not root:
            return 0

        def left_depth(node):
            left_levels = 0
            while node:
                node = node.left
                left_levels += 1

            return left_levels

        def right_depth(node):
            right_levels = 0
            while node:
                node = node.right
                right_levels += 1

            return right_levels

        left_depth_value = left_depth(root)
        right_depth_value = right_depth(root)
        if left_depth_value == right_depth_value:
            return (1 << left_depth_value) - 1

        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
