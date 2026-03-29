class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        graph = {}
        for ch in t:
            graph[ch] = graph.get(ch, 0) + 1
        
        have, need = 0, len(graph)
        start = 0
        freq = {}
        res, reslen = [-1, -1], float('infinity')
        for r in range(len(s)):
            char = s[r]
            freq[char] = freq.get(char, 0) + 1
            if char in graph and graph[char] == freq[char]:
                have += 1
            
            while have == need:
                if (r - start + 1) < reslen:
                    res = [start, r]
                    reslen = r - start + 1
                prev = s[start]
                freq[prev] -= 1
                if prev in graph and freq[prev] < graph[prev]:
                    have -= 1
                start += 1

        if reslen == float("inf"):   
            return ""
        start, r = res
        return s[start: r+1]
            