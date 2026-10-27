class TrieNode:
    def __init__(self):
        self.children = {} # word -> TrieNode()
        self.endOfWord = False

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        root = TrieNode()
        for word in dictionary:
            node = root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.endOfWord = True
        n = len(s)
        dp = [0] * (n+1)
        for i in range(n-1, -1, -1):
            dp[i] = 1 + dp[i+1]
            node = root
            for j in range(i,n):
                if s[j] not in node.children:
                    break
                node = node.children[s[j]]
                if node.endOfWord:
                    dp[i] = min(dp[i], dp[j+1])
        return dp[0]
