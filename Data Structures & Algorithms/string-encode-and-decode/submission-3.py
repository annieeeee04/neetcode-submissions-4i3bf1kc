class Solution:

    def encode(self, strs: List[str]) -> str:
        out = ''
        for s in strs:
            out += str(len(s)) + '#' + s  # "3#abc4#test"
        return out

    def decode(self, s: str) -> List[str]:
        out = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            out.append(s[j+1: j+1+length])
            i = j+1+length
        return out