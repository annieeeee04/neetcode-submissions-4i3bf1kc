class MyHashSet:

    def __init__(self):
        self.size = 1009
        self.buckets = [[] for _ in range(self.size)]

    def _bucket(self, key):
        return self.buckets[key % self.size]

    def add(self, key: int) -> None:
        a = self._bucket(key)
        if key not in a:
            a.append(key)

    def remove(self, key: int) -> None:
        b = self._bucket(key)
        if key in b:
            b.remove(key)

    def contains(self, key: int) -> bool:
        return key in self._bucket(key)


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)