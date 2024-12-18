"""
@complexity
time: O(n)
space: O(h)
"""

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: bool
        """

        def dfs(root):
            lookup = set()
            stack = [root]
            while stack:
                node = stack.pop()
                if k - node.val in lookup:
                    return True
                lookup.add(node.val)
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)

            return False

        return dfs(root)
