class TimeMap:

    def __init__(self):
        self.cache = {} # key -> (value, timestamp)

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.cache:
            self.cache[key] = []
        
        self.cache[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.cache:
            return ""
        
        stores = self.cache[key]
        l, r = 0, len(stores) - 1
        res = ''
        while l <= r:
            mid = (l+r) // 2
            if stores[mid][1] <= timestamp:
                res = stores[mid][0]
                l = mid + 1
            else:
                r = mid - 1
        return res