# Time: O(n² · L), n² (j, i) pairs, each slice + hash costs up to O(L), L = longest word
# Space: O(n + total dictionary size)
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True                      # empty prefix is trivially segmentable
        words = set(wordDict)

        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in words:     # s[j:i] = last word of the prefix
                    dp[i] = True
                    break
        return dp[n]

        # 中文：dp[i] 表示前 i 个字符能否拆成单词，枚举最后一个单词的起点 j