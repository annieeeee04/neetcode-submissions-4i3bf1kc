class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        good = set()

        for tri in triplets:
            if (tri[0] > target[0] or
                tri[1] > target[1] or
                tri[2] > target[2]):
                continue
            
            for i, v in enumerate(tri):
                if v == target[i]:
                    good.add(i)
        
        return len(good) == 3