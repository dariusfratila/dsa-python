"""
@complexity
time: O(n)
space: O(h)
"""


class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: Optional[TreeNode]
        :type root2: Optional[TreeNode]
        :rtype: bool
        """

        def dfs(root):
            leaves = []
            stack = [root]
            while stack:
                node = stack.pop()
                if node:
                    if not node.left and not node.right:
                        leaves.append(node.val)
                    if node.left:
                        stack.append(node.left)
                    if node.right:
                        stack.append(node.right)

            return leaves

        first_tree = dfs(root1)
        second_tree = dfs(root2)

        return first_tree == second_tree
