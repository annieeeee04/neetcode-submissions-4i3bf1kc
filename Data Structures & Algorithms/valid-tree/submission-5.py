# Time: O(N + E)
# Space: O(N + E) , hashmap

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Early exit: a valid tree must have exactly n-1 edges
        if len(edges) != n-1:
            return False
        
        graph = {i:[] for i in range(n)}
        visit = set()
        visit.add(0)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        q = deque([[0,-1]])
        while q:
            node, prev = q.popleft()
            for edg in graph[node]:
                # for undirected tree, going back and forward between 
                # two nodes is not considered as a loop
                if edg == prev:
                    continue
                # when there's more than 2 nodes involved, 
                # we detect a loop
                if edg in visit:
                    return False
                q.append([edg, node])
                visit.add(edg)

        # Final check: len(visit) == n ensures all nodes are connected
        return len(visit) == n