class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        out = [0] * len(temperatures)
        stack = [] # [idx, temp]

        for i, t in enumerate(temperatures):
            while stack and stack[-1][1] < t:
                idx, temp = stack.pop()
                out[idx] = i - idx
            stack.append([i, t])
        return out