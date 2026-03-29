class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs:
            res += str(len(s)) + '#' + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1 

            # j -> the position of #
            length = int(s[i:j])
            start, end = j+1, j+1+length
            res.append(s[start:end])
            i = end

        return res