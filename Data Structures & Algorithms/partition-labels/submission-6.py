class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIdx = {}
        for i, char in enumerate(s):
            lastIdx[char] = i
        
        l = 0
        out = []
        while l < len(s):
            last = lastIdx[s[l]]
            for i in range(l, len(s)):
                last = max(last, lastIdx[s[i]])
                if last == i:
                    out.append(last-l+1)
                    l = last + 1
                    break
        return out