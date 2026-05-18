"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
# Iterative
# Time:
# Space: 
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        queue = deque([node])
        cloned = {node: Node(node.val)}

        while queue:
            cur = queue.popleft()
            
            for nb in cur.neighbors:
                if nb not in cloned:
                    cloned[nb] = Node(nb.val)
                    queue.append(nb)
                cloned[cur].neighbors.append(cloned[nb])

        return cloned[node]