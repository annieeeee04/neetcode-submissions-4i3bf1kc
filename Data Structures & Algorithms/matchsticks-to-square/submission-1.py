class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total = sum(matchsticks)
        if total % 4 != 0:
            return False
        target = total // 4
        sides = [0] * 4
        matchsticks.sort(reverse=True)

        def backtrack(i):
            if i == len(matchsticks):
                return True

            stick = matchsticks[i]
            for j in range(4):
                if sides[j] + stick <= target:
                    sides[j] += stick
                    if backtrack(i+1):
                        return True
                    sides[j] -= stick
            return False
        
        return backtrack(0)