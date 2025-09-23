class DetectSquares:

    def __init__(self):
        self.ptsCount = defaultdict(int)
        self.pts = []

    def add(self, point: list[int]) -> None:
        self.ptsCount[tuple(point)] += 1
        self.pts.append(point)  # append instead of overwrite

    def count(self, point: list[int]) -> int:
        x, y = point
        res = 0
        
        for px, py in self.pts:
            # check if a valid square side
            if x == px or y == py or abs(px-x) != abs(py-y):
                continue
            res += self.ptsCount[(x, py)] * self.ptsCount[(px, y)]
        
        return res

# Time - Add: O(1)

# Time - Count: O(n) where n = number of points added so far

# Space: O(n)