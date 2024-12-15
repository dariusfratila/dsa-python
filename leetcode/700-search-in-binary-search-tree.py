"""
@complexity
time: O(h)
space: O(1)
"""


class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :rtype: Optional[TreeNode]
        """

        while root:
            if root.val == val:
                return root
            elif val < root.val:
                root = root.left
            else:
                root = root.right

        return None


"""
@complexity
time: O(h)
space: O(h)
"""


class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :rtype: Optional[TreeNode]
        """

        def dfs(root):
            stack = [root]
            while stack:
                current = stack.pop()
                if current.val == val:
                    return current
                if val < current.val and current.left:
                    stack.append(current.left)
                elif val > current.val and current.right:
                    stack.append(current.right)
            return None

        return dfs(root)
