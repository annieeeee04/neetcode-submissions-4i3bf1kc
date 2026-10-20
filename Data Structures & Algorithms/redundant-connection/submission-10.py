class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = list(range(n+1))
        rank = [1] * (n+1)

        def find(i):
            if parent[i] != i:
                parent[i] = find(parent[i])
            return parent[i]
        
        def union(u,v):
            rootA, rootB = find(u), find(v)
            if rootA == rootB:
                return False
            
            if rank[rootA] < rank[rootB]:
                parent[rootA] = rootB
            elif rank[rootB] < rank[rootA]:
                parent[rootB] = rootA
            else:
                parent[rootB] = rootA
                rank[rootA] += 1
            return True
        
        for u,v in edges:
            if not union(u,v):
                return [u,v]
