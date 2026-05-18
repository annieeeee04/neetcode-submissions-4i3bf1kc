# 2^n possible partitions (each position is either a cut or not)
# O(n) for palindrome check sub[::-1] and path copy
# --> Time: O(n * 2^n)

# Space: O(n)

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        out = []
        def backtrack(i, path):
            if i >= len(s):
                out.append(path[:])

            for j in range(i, len(s)):
                sub = s[i:j+1]
                if sub == sub[::-1]:
                    path.append(sub)
                    backtrack(j+1, path)
                    path.pop()
        backtrack(0, [])
        return out
