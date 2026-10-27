class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        queue = deque()
        visited = set(deadends)                       
        if "0000" in visited:
            return -1
        
        q = deque([("0000", 0)])
        visited.add('0000')
        while q:
            state, turns = q.popleft()
            if state == target:
                return turns
            
            for i in range(4):
                d = int(state[i])
                for nd in ((d + 1) % 10, (d - 1) % 10):
                    nxt = state[:i] + str(nd) + state[i+1:]
                    if nxt not in visited:
                        visited.add(nxt)
                        q.append((nxt, turns+1))
        return -1