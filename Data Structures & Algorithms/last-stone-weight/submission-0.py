class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort()
            first = stones.pop()
            second = stones.pop()
            left = first - second
            if left == 0:
                continue
            stones.append(left)
        if len(stones) == 0:
            return 0
        else:
            return stones[0]