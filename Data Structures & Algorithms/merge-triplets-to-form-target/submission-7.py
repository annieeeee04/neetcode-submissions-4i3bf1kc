class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        cur = [float('-inf')] * 3

        for t in triplets:
            if (t[0] > target[0] or 
                t[1] > target[1] or 
                t[2] > target[2]):
                continue
            for i in range(3):
                cur[i] = max(cur[i], t[i])
            
        return cur == target