class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_len = 0
        path = set()
        for n in nums:
            if n not in path:
                path.add(n)

        for n in nums:
            cnt = 0
            if n-1 not in path:
                while n in path:
                    cnt += 1
                    n += 1
                max_len = max(max_len, cnt)
        
        return max_len