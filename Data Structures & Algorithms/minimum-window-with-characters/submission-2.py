class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        
        graph1, graph2 = {}, {}
        for char in t:
            graph1[char] = graph1.get(char, 0) + 1
        
        need = len(graph1)
        best = float('inf')
        res = [0,0]
        start = 0
        have = 0
        for r in range(len(s)):
            char = s[r]
            graph2[char] = graph2.get(char, 0) + 1
            if char in graph1 and graph1[char] == graph2[char]:
                have += 1
            
            while have == need:
                if (r - start + 1) < best:
                    best = r - start + 1
                    res = [start, r]
                last = s[start]
                graph2[last] -= 1
                if graph2.get(last,0) < graph1.get(last,0):
                    have -= 1
                start += 1
        if best == float('inf'):
            return ""
        
        left, right = res
        return s[left:right+1]