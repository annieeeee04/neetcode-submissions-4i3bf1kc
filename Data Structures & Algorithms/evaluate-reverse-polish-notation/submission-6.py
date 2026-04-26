class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        path = []

        for t in tokens:
            if t == '+':
                prev1 = path.pop()
                prev2 = path.pop()
                path.append(prev1 + prev2)
            elif t == '-':
                prev1 = path.pop()
                prev2 = path.pop()
                path.append(prev2 - prev1)
            elif t == '*':
                prev1 = path.pop()
                prev2 = path.pop()
                path.append(prev1 * prev2)
            elif t == '/':
                prev1 = path.pop()
                prev2 = path.pop()
                path.append(int(prev2 / prev1))
            else:
                path.append(int(t))
        return path[0]