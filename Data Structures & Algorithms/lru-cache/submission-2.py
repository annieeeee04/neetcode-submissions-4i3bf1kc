class Node:

    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity
        self.left = Node(0,0)
        self.right = Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = node
        nxt.prev = node
        node.prev = prev
        node.next = nxt

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.remove(node)
        self.insert(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            new_node = Node(key, value)
            self.cache[key] = new_node
            self.insert(new_node)
        else:
            node = self.cache[key]
            node.val = value
            self.remove(node)
            self.insert(node)
        
        if len(list(self.cache.keys())) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
