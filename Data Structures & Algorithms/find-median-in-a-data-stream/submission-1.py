class MedianFinder:

    def __init__(self):
        self.arr = []

    def addNum(self, num: int) -> None:
        l, r = 0, len(self.arr)
        while l < r:
            mid = (l + r) // 2
            val = self.arr[mid]
            if num > val:
                l = mid + 1
            else:
                r = mid
        self.arr.insert(l, num)

    def findMedian(self) -> float:
        n = len(self.arr)
        half = n // 2
        if n % 2:
            return self.arr[half]
        else:
            return (self.arr[half-1] + self.arr[half]) / 2
        