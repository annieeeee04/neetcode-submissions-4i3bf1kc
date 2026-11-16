# Time: O(n)
# Space: O(1)
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        out = []
        for a in asteroids:
            # right-mover meets left-mover
            while out and out[-1] > 0 > a:
                # top is smaller: it explodes, a continues
                if out[-1] < -a:
                    out.pop()
                    continue
                # same size: both explode
                if out[-1] == -a:
                    out.pop()
                break  # a is destroyed (or both gone)
            else:
                out.append(a)
        return out