"""
@complexity
time: O(n)
space: O(n)
"""


class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.total_tilt = 0

        def postorder(node):
            if not node:
                return 0

            left_sum = postorder(node.left)
            right_sum = postorder(node.right)

            tilt = abs(left_sum - right_sum)

            self.total_tilt += tilt

            return node.val + left_sum + right_sum

        postorder(root)
        return self.total_tilt
