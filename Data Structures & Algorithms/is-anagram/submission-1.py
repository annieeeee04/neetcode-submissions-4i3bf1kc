class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        graph1, graph2 = {}, {}
        for char in s:
            graph1[char] = graph1.get(char,0) + 1
        for char in t:
            graph2[char] = graph2.get(char, 0) + 1
        
        return graph1 == graph2