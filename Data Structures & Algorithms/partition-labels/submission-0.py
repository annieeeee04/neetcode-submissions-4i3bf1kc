class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        out = []
        end = 0
        size = 0
        lastIdx = defaultdict(list)
        for i in range(len(s)):
            lastIdx[s[i]].append(i)
        
        for start in range(len(s)):
            char = s[start]
            end = max(lastIdx[char][-1],end)
            size += 1
            if start == end:
                out.append(size)
                size = 0
                
        return out
