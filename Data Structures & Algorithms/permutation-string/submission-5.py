# Time: O(m) , length of s2
# Space: O(26)

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        graph1, graph2 = {}, {}
        n, m = len(s1), len(s2)

        for char in s1:
            graph1[char] = graph1.get(char,0) + 1
        
        for char in s2[:n]:
            graph2[char] = graph2.get(char,0) + 1
        
        if graph1 == graph2: return True
        
        for i in range(n, m):
            left = i - n
            last = s2[left]
            graph2[last] -= 1
            if graph2[last] == 0:
                del graph2[last]
            
            new = s2[i]
            graph2[new] = graph2.get(new,0) + 1
            if graph1 == graph2:
                return True
        return False