# Time: O(n)
# Space: O(1) extra (at most 26 keys), O(n) if the output list is counted

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIdx = {}
        for i, char in enumerate(s):
            lastIdx[char] = i
        
        out = []
        last = 0
        l = 0
        while l < len(s):
            for i in range(l, len(s)):
                last = max(last, lastIdx[s[i]])
                if last == i:
                    out.append(last-l+1)
                    l = last + 1
                    break
        return out