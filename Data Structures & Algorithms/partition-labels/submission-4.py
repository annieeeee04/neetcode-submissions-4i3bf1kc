# Time: O(n)
# Space: O(k)

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIdx = {}
        for i, char in enumerate(s):
            lastIdx[char] = i
        
        out = []
        end = 0
        size = 0
        for start in range(len(s)):
            char = s[start]
            end = max(end, lastIdx[char])
            size += 1
            if start == end:
                out.append(size)
                size = 0
        
        return out