class Solution:
    def calPoints(self, operations: List[str]) -> int:
        out = []
        for op in operations:
            if op == '+':
                first = out[-1]
                second = out[-2]
                out.append(first + second)
            elif op == 'C':
                out.pop()
            elif op == 'D':
                digit = out[-1]
                out.append(digit * 2)
            else:
                out.append(int(op))
        return sum(out)