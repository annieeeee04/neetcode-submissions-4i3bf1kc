# monotonic deque
# Time: O(n)
# Space: O(k)

from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque() # collection of indices
        res = []
        l = 0

        for r in range(len(nums)):
            # pop smaller values from the back — they can never be
            # the max while nums[r] is still in the window
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            # pop the front if it's fallen out of the window
            if q[0] < l:
                q.popleft()
            if r - l + 1 >= k:
                res.append(nums[q[0]])
                l += 1
        return res
