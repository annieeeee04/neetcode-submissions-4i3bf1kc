class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        path = []
        for a in asteroids:
            while path and path[-1] > 0 > a:
                if path[-1] < -a:
                    path.pop()
                    continue
                if path[-1] == -a:
                    path.pop()
                break
            else:
                path.append(a)
        return path