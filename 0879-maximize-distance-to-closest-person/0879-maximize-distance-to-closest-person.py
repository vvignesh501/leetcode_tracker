class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        res, prev, L = 0, -1, len(seats)
        for i, n in enumerate(seats):
            if n == 1:
                if prev == -1:
                    dist = i
                else:
                    dist = (i - prev)//2

                res = max(res, dist)
                prev = i
                
        if not seats[i]: #check last seat edge-case
            res = max(res, i - prev)

        return res