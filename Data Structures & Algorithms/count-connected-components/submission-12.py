class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = list(range(n))
        rank = [0] * n
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        def union(a,b):
            rootA, rootB = find(a), find(b)
            if rootA == rootB:
                return False

            if rootA != rootB:
                if rank[rootA] < rank[rootB]:
                    parent[rootA] = rootB
                elif rank[rootB] < rank[rootA]:
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
        