class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        rank = [0] * n
        parent = list(range(n))

        def find(node):
            if node != parent[node]:
                parent[node] = find(parent[node])
            return parent[node]
        
        def union(u,v):
            rootA, rootB = find(u), find(v)
            if rootA == rootB:
                return False
            else:
                if parent[rootA] < parent[rootB]:
                    parent[rootA] = rootB
                elif parent[rootB] < parent[rootA]:
                    parent[rootB] = rootA
                else:
                    parent[rootB] = rootA
                    rank[rootA] += 1
                return True
        
        num = n
        for u,v in edges:
            if union(u,v):
                num -= 1
        return num