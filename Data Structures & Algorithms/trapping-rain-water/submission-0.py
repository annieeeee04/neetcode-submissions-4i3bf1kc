class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        lMax, rMax = 0, 0
        water = 0

        while l <= r:
            if lMax <= rMax:
                if height[l] > lMax:
                    lMax = height[l]
                else:
                    water += lMax - height[l]
                l += 1
            else:
                if height[r] > rMax:
                    rMax = height[r]
                else:
                    water += rMax - height[r]
                r -= 1
        return water