"""
@complexity
time: O(n)
space: O(h)
"""

class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        INF = 10 ** 20

        def preorder(node):
            if not root:
                return

            if root.val != node.val:
                return node.val

            if node.right:
                return min(preorder(node.left), preorder(node.right))

            return INF

        r = preorder(root)
        if r >= INF:
            return -1

        return r
