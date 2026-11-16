class TimeMap:

    def __init__(self):
        self.timeMap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMap[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timeMap:
            return ''
        else:
            values = self.timeMap.get(key)
            l, r = 0, len(values) - 1
            ans = ''
            while l <= r:
                mid = (l+r) // 2
                t = values[mid][1]
                if t <= timestamp:
                    ans = values[mid][0]
                    l = mid + 1
                else:
                    r = mid - 1
            return ans
