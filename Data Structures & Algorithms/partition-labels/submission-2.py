class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        out = []
        size = 0
        end = 0
        lastIdx = {}
        for i in range(len(s)):
            lastIdx[s[i]] = i
        
        for start in range(len(s)):
            char = s[start]
            end = max(end, lastIdx[char])
            size += 1
            if start == end:
                out.append(size)
                size = 0
        
        return out