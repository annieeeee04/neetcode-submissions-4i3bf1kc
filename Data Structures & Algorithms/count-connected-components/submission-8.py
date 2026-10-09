class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = list(range(n))
        rank = [0] * n

        def find(node):
            if node != parent[node]:
                parent[node] = find(parent[node])
            return parent[node]
        
        def union(u,v):
            rootA, rootB = find(u), find(v)
            if rootA != rootB:
                if rank[rootA] < rank[rootB]:
                    parent[rootA] = rootB
                elif rank[rootB] < rank[rootA]:
                    parent[rootB] = rootA
                else:
                    parent[rootB] = rootA
                    rank[rootA] += 1
        
        for u, v in edges:
            union(u,v)
        
        return len(set(find(i) for i in range(n)))
