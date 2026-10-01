# Time: O(n log n), dominated by the sort
# Space: O(n), stack can hold up to n fleet times

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # sort front-to-back (closest to target first) —
        # a car can only ever catch up to the fleet ahead of it
        cars = sorted(zip(position, speed), reverse=True)
        stack = []

        for pos, spd in cars:
            time = (target - pos) / spd
            # time > stack[-1]: this car takes longer to reach the
            # target on its own than the fleet ahead — can never
            # catch up, so it becomes its own new fleet.
            # otherwise it catches up and merges, so push nothing.
            if not stack or time > stack[-1]:
                stack.append(time)

        return len(stack)