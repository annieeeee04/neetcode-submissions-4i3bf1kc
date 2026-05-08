class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = list(range(n+1))    
        rank = [0] * (n+1)

        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node]) # path compression
            return parent[node]
        
        def union(a,b):
            rootA, rootB = find(a), find(b)

            # same root -> cycle found!
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
        
        for a, b in edges:
            if not union(a,b):
                return [a,b] # this edge caused the cycle