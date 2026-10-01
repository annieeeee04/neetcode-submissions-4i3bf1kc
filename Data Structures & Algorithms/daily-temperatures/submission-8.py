# monotonic decreasing stack
# stack is LIFO, so the top is stack[-1]

# Time: O(n), each index pushed and popped at most once
# Space: O(n), worst case strictly decreasing temps never get popped
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for i, t in enumerate(temperatures):
            # pop ALL entries smaller than t, not just the top one —
            # a single warmer day can resolve multiple pending days at once
            while stack and stack[-1][1] < t:
                idx, temp = stack.pop()
                res[idx] = i - idx
            # push current day; stays until a warmer day resolves it
            stack.append([i, t])
        return res

