"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return None
        
        def dfs(node):
            stack = [node]
            cloned = {node: Node(node.val)}

            while stack:
                cur = stack.pop()

                for nb in cur.neighbors:
                    if nb not in cloned:
                        cloned[nb] = Node(nb.val)
                        stack.append(nb)
                    cloned[cur].neighbors.append(cloned[nb])
                    
            return cloned[node]
        
        return dfs(node)