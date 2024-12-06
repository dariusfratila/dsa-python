"""
@complexity
time: O(n)
space: O(h)
"""


class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[float]
        """

        if not root:
            return []

        average = []
        deq = deque([root])

        while deq:
            level_sum = 0
            level_count = len(deq)

            for _ in range(level_count):
                node = deq.popleft()
                level_sum += node.val
                if node.left:
                    deq.append(node.left)
                if node.right:
                    deq.append(node.right)

            average.append(level_sum / float(level_count))

        return average
