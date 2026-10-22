"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
# Time: O(V + E)
# Space: O(V + E)
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        queue = deque([node])
        copies = {node: Node(node.val)}

        while queue:
            cur = queue.popleft()
            for nb in cur.neighbors:
                if nb not in copies:
                    copies[nb] = Node(nb.val)
                    queue.append(nb)
                copies[cur].neighbors.append(copies[nb])
        
        return copies[node]