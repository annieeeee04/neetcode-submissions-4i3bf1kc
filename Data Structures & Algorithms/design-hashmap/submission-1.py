class MyHashMap:

    def __init__(self):
        self.size = 1009
        self.buckets = [[] for _ in range(self.size)]

    def _bucket(self, key):
        return self.buckets[key % self.size]

    def put(self, key: int, value: int) -> None:
        target = self._bucket(key)
        for pair in target:
            if pair[0] == key:
                pair[1] = value
                return
        target.append([key, value])

    def get(self, key: int) -> int:
        target = self._bucket(key)
        for pair in target:
            if pair[0] == key:
                return pair[1]
        return -1

    def remove(self, key: int) -> None:
        target = self._bucket(key)
        for i, pair in enumerate(target):
            if pair[0] == key:
                target.pop(i)
                return


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)