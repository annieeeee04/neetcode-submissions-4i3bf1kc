class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(opening, close, path):
            if opening == close == n:
                cur = ''.join(path)
                res.append(cur)
                return
            
            if opening < n:
                path.append('(')
                backtrack(opening+1, close, path)
                path.pop()
            
            if close < opening:
                path.append(')')
                backtrack(opening, close+1, path)
                path.pop()
        
        backtrack(0,0,[])
        return res