class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        rank = {ch: i for i, ch in enumerate(order)}

        for i in range(len(words) - 1):
            a, b = words[i], words[i + 1]
            for j in range(min(len(a), len(b))):
                if a[j] != b[j]:
                    if rank[a[j]] > rank[b[j]]:
                        return False
                    break
            else:
                if len(a) > len(b):
                    return False
        return True