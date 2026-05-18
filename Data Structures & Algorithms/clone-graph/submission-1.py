"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        cloned = {} # node -> clone

        def dfs(node):
            if not node:
                return None

            if node in cloned:
                return cloned[node]
            
            copy = Node(node.val)
            cloned[node] = copy
            for nb in node.neighbors:
                copy.neighbors.append(dfs(nb))
            
            return copy
        
        return dfs(node)