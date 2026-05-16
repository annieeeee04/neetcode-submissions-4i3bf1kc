class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIdx = {}
        for i, char in enumerate(s):
            lastIdx[char] = i
        
        out = []
        l = 0
        while l < len(s):
            last = lastIdx[s[l]]
            for j in range(l, len(s)):
                last = max(last, lastIdx[s[j]])
                if last == j:
                    out.append(last-l+1)
                    l = last + 1
                    break
        return out