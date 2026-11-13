class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m, n = len(word1), len(word2)
        out = []
        for i in range(min(m,n)):
            out.append(word1[i])
            out.append(word2[i])
        if m < n:
            out.append(word2[i+1:])
        else:
            out.append(word1[i+1:])
        
        return ''.join(out)