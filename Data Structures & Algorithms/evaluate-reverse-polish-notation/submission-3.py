class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        path = []
        for i, t in enumerate(tokens):
            if t == '+':
                first = path.pop()
                second = path.pop()
                path.append(first + second)
            elif t == "-":
                first = path.pop()
                second = path.pop()
                path.append(second - first)
            elif t == "*":
                first = path.pop()
                second = path.pop()
                path.append(first * second)
            elif t == "/":
                first = path.pop()
                second = path.pop()
                path.append(int(second / first))
            else:
                path.append(int(t))
        
        return int(path[0])