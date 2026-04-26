# Time: O(\frac{4^n}{\sqrt{n}})
# Space: O(n)

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        out = []

        def backtrack(l, r, path):
            if l == r == n:
                cur = ''.join(path)
                out.append(cur)
                return

            if l < n:
                path.append('(')
                backtrack(l+1, r, path)
                path.pop()
            if r < l:
                path.append(')')
                backtrack(l, r + 1, path)
                path.pop()
        
        backtrack(0, 0, [])
        return out