class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        m, n = len(num1), len(num2)
        out = [0] * (m + n)

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                mul = int(num1[i]) * int(num2[j])
                total = mul + out[i+j+1] 
                out[i+j+1] = total % 10
                out[i+j] += total // 10
        
        res = ''.join(map(str, out)).lstrip('0')
        return res or '0'