"""
@complexity
time: O(n)
space: O(h)
"""

class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        res = 0
        queue = deque([(root, str(root.val))])

        while queue:
            node, path_str = queue.popleft()

            if not node.left and not node.right:
                res += int(path_str, 2)
            else:
                if node.left:
                    queue.append((node.left, path_str + str(node.left.val)))
                if node.right:
                    queue.append((node.right, path_str + str(node.right.val)))

        return res
