"""
@complexity
time: O(n)
space: O(n)
"""


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return

        start_node = node
        stack = [start_node]

        visited = set()
        visited.add(start_node)

        old_new_graph = {}

        while stack:
            node = stack.pop()
            old_new_graph[node] = Node(val=node.val)

            for neighbor in node.neighbors:
                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.append(neighbor)

        for old_node, new_node in old_new_graph.items():
            for neighbor in old_node.neighbors:
                new_neighbor = old_new_graph[neighbor]
                new_node.neighbors.append(new_neighbor)

        return old_new_graph[start_node]
