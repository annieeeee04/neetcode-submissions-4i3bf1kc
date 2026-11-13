class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = {0:1}

        cnt = 0
        cur = 0
        for n in nums:
            cur += n
            if cur - k in prefix:
                cnt += prefix.get(cur-k)
            prefix[cur] = prefix.get(cur,0) + 1
        return cnt