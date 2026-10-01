class Solution:
    def isValid(self, s: str) -> bool:
        dict = {')':'(', ']':'[', '}':'{'}
        record = []

        for char in s:
            if char not in dict:
                record.append(char)
            else:
                if not record:
                    return False
                elif record[-1] != dict[char]:
                    return False
                else:
                    record.pop()
        if len(record) == 0:
            return True
        else:
            return False