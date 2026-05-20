class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        lMax, rMax = 0, 0

        water = 0
        while l <= r:
            if lMax < rMax:
                if height[l] < lMax:
                    water += lMax - height[l]
                else:
                    lMax = height[l]
                l += 1
            else:
                if height[r] < rMax:
                    water += rMax - height[r]
                else:
                    rMax = height[r]
                r -= 1
            
        return water