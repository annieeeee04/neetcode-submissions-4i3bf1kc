class TimeMap:

    def __init__(self):
        self.cache = {} # key -> [timestamp, value]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.cache:
            self.cache[key] = []
        self.cache[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.cache:
            return ""
        
        arr = self.cache[key]
        l, r = 0, len(arr)-1
        ans = ""
        while l <= r:
            mid = (l + r) // 2
            if arr[mid][0] <= timestamp:
                ans = arr[mid][1]
                l = mid + 1
            else:
                r = mid - 1
        return ans