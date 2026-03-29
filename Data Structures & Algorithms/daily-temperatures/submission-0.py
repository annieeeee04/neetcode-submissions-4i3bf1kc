class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        out = [0] * n
        stack = []

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                temp, idx = stack.pop()
                out[idx] = i - idx
            stack.append((t, i))
        
        return out