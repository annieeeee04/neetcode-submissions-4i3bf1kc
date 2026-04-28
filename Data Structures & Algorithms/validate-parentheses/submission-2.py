class Solution:
    def isValid(self, s: str) -> bool:
        graph = {')':'(', ']':'[', '}':'{'}
        path = []
        for char in s:
            if char in graph:
                if not path:
                    return False
                
                last = path[-1]
                if graph[char] != last:
                    return False
                else:
                    path.pop()
            else:
                path.append(char)
                
        return len(path) == 0