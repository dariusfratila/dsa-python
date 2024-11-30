"""
@complexity
time: O(n)
space: O(h)
"""


class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """

        res = []

        def preorder(node):
            if not node:
                return
            res.append(node.val)
            preorder(node.left)
            preorder(node.right)

        preorderTrav = preorder(root)
        return res
