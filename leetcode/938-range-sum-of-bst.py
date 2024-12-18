"""
@complexity
time: O(n)
space: O(h)
"""


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        deq = deque([root])
        total_sum = 0
        while deq:
            for _ in range(len(deq)):
                node = deq.popleft()
                if low <= node.val <= high:
                    total_sum += node.val

                if node.left and low <= node.val:
                    deq.append(node.left)
                if node.right and high >= node.val:
                    deq.append(node.right)

        return total_sum
