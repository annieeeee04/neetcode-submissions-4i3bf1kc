# Time: O(n)
# Space: O(n)

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # traverse in the reverse order, 
        # the we go through cars from the one closest to the target
        # which is most likely to reach the target the first
        # thus we can identify the fleet correctly
        cars = sorted(zip(position, speed), reverse = True)
        stack = []

        for p, s in cars:
            time = (target - p) / s
            stack.append(time)

            if len(stack) > 1 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)