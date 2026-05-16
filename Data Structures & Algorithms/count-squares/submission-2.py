class CountSquares:

    def __init__(self):
        self.points = defaultdict(int)

    def add(self, point: List[int]) -> None:
        px, py = point
        self.points[(px, py)] += 1

    def count(self, point: List[int]) -> int:
        cnt = 0
        px, py = point
        for (dx, dy), dcnt in self.points.items():
            if (abs(px - dx) != abs(py - dy) or 
                px == dx or py == dy):
                continue
            cnt += dcnt * self.points.get((px, dy), 0) * self.points.get((dx, py), 0)
        return cnt
