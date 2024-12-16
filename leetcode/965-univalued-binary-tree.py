"""
@complexity
time: O(n)
space: O(h)
"""


class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        def bfs(root):
            deq = deque([root])
            while deq:
                target_value = root.val
                for _ in range(len(deq)):
                    node = deq.popleft()
                    if node.val != target_value:
                        return False
                    if node.left:
                        deq.append(node.left)
                    if node.right:
                        deq.append(node.right)

            return True

        return bfs(root)
