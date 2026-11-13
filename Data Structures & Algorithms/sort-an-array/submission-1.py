import random
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def quick(lo, hi):
            if lo >= hi:
                return
            p = nums[random.randint(lo, hi)]
            # [lo,lt) < p, [lt,i) == p, (gt,hi] > p
            lt, i, rt = lo, lo, hi
            while i <= rt:
                if nums[i] < p:
                    nums[lt], nums[i] = nums[i], nums[lt]
                    lt += 1
                    i += 1
                elif nums[i] == p:
                    i += 1
                else:
                    nums[i], nums[rt] = nums[rt], nums[i]
                    # don't advance i: the swapped-in value is unchecked
                    rt -= 1
            quick(lo, lt - 1)
            quick(rt + 1, hi)

        quick(0, len(nums)-1)
        return nums