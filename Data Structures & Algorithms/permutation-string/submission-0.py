class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m,n = len(s1), len(s2)
        if m > n:
            return False
        
        graph = {}
        for char in s1:
            graph[char] = graph.get(char, 0) + 1
        
        freq = {}
        for char in s2[:m]:
            freq[char] = freq.get(char, 0) + 1
        
        if freq == graph:
            return True
        
        for i in range(m, n):
            past = s2[i-m]
            cur = s2[i]
            freq[past] -= 1
            if freq[past] == 0:
                del freq[past]
                
            freq[cur] = freq.get(cur, 0) + 1
            if freq == graph:
                return True
        
        return False
