# Time: O(m * n)
# Space: O(m * n)

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        cache = {} # (i,j) -> cnt

        def dfs(i, j):
            if i == len(word1):
                return len(word2) - j
            if j == len(word2):
                return len(word1) - i
            
            if (i,j) in cache:
                return cache[(i,j)]
            
            if word1[i] == word2[j]:
                res = dfs(i+1, j+1)
            else:
                insert = 1 + dfs(i, j+1)
                delete = 1 + dfs(i+1, j)
                replace = 1 + dfs(i+1, j+1)
                res = min(insert, delete, replace)
            
            cache[(i,j)] = res
            return res

        return dfs(0,0)