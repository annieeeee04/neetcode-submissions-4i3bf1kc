# opening can’t exceed n
# closing can’t exceed opening
# done when opening == closing == n
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(l, r, path):
            if l == r == n:
                cur = ''.join(path)
                res.append(cur)
                return
            
            if l < n:
                path.append("(")
                backtrack(l+1, r, path)
                path.pop()
            
            if r < l:
                path.append(")") 
                backtrack(l, r+1, path)
                path.pop()

        backtrack(0,0,[])
        return res