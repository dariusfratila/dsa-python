"""
@complexity
time: O(n)
space: O(n)
"""


class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: Optional[TreeNode]
        :type x: int
        :type y: int
        :rtype: bool
        """

        stack = [(root, None, 0)]
        x_parent = None
        y_parent = None
        while stack:
            node, parent, level = stack.pop()

            if node.val == x:
                x_parent = (parent, level)
            if node.val == y:
                y_parent = (parent, level)

            if node.left:
                stack.append([node.left, node, level + 1])
            if node.right:
                stack.append([node.right, node, level + 1])

            if x_parent and y_parent:
                break

        if x_parent[0] != y_parent[0] and x_parent[1] == y_parent[1]:
            return True

        return False
