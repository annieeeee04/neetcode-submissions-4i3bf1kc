class Solution:
    def checkValidString(self, s: str) -> bool:
        minL, maxL = 0, 0
        for char in s:
            if char == '(':
                minL += 1
                maxL += 1
            elif char == ')':
                if not maxL:
                    return False
                else:
                    minL -= 1
                    if minL < 0:
                        minL = 0
                    maxL -= 1
                    if maxL < 0:
                        return False
            else:
                minL -= 1
                if minL < 0:
                    minL = 0
                maxL += 1
        return minL == 0
            