# Union Join
# Time: O(E)

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = list(range(n+1))
        rank = [1] * (n+1)
        
        # O(a) ~= O(1)
        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node])
            return parent[node]
        
        # O(1)
        def union(a,b):
            rootA, rootB = find(a), find(b)
            if rootA == rootB:
                return False
            
            if rank[rootA] < rank[rootB]:
                parent[rootA] = rootB
            elif rank[rootA] > rank[rootB]:
                parent[rootB] = rootA
            else:
                parent[rootB] = rootA
                rank[rootA] += 1
            return True
        
        for u,v in edges:
            if not union(u,v): 
                return [u,v]