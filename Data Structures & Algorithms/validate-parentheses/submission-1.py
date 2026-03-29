class Solution:
    def isValid(self, s: str) -> bool:
        graph = {')':'(', ']':'[', '}':'{'}
        cur = []

        for char in s:
            if char in graph:
                if cur == []:
                    return False
                    
                last = cur[-1]
                if last != graph[char]:
                    return False
                else:
                    cur.pop()
            else:
                cur.append(char)
        
        return cur == []