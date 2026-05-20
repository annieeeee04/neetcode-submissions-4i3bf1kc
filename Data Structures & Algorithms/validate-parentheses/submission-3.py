class Solution:
    def isValid(self, s: str) -> bool:
        graph = {')':'(', ']':'[', '}':'{'}
        path = []

        for char in s:
            if char in graph:
                if not path:
                    return False
                else:
                    if path[-1] != graph[char]:
                        return False
                    else:
                        path.pop()
            else:
                path.append(char)
        return len(path) == 0