"""
@complexity
time: O(n)
space: O(h)
"""

class Solution(object):
    def mergeTrees(self, root1, root2):
        """
        :type root1: Optional[TreeNode]
        :type root2: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """

        if not root1 and not root2:
            return None

        value1 = root1.val if root1 else 0
        value2 = root2.val if root2 else 0

        root = TreeNode(value1 + value2)

        root.left = self.mergeTrees(root1.left if root1 else None, root2.left if root2 else None)
        root.right = self.mergeTrees(root1.right if root1 else None, root2.right if root2 else None)

        return root




