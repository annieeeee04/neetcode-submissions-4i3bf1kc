# Union Find
# Time: O(E)
# Space: O(E)

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = list(range(n+1))
        rank = [0] * (n+1)

        # B/C path compression, the find is almost O(1)
        def find(node):
            if node != parent[node]:
                parent[node] = find(parent[node])
            return parent[node]

        # union does 2 find, so O(1) as well
        def union(a,b):
            rootA, rootB = find(a), find(b)

            if rootA == rootB:
                return False
            
            # A is shorter than B → attach A under B
            if rank[rootA] < rank[rootB]:
                parent[rootA] = rootB
            # B is shorter than A → attach B under A
            elif rank[rootA] > rank[rootB]:
                parent[rootB] = rootA
            else:
                parent[rootB] = rootA
                rank[rootA] += 1
            return True
        
        # worst case go through all edges
        # do union for each edge -> O(E)
        for u,v in edges:
            if not union(u,v):
                return [u,v]
