class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fives = 0
        tens = 0

        for b in bills:
            if b == 5:
                fives += 1
            elif b == 10:
                if not fives:
                    return False
                else:
                    fives -= 1
                    tens += 1
            else:
                if fives and tens:
                    fives -= 1
                    tens -= 1
                elif fives >= 3:
                    fives -= 3
                else:
                    return False
        return True