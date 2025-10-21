class Solution:
    def maxDistToClosest(self, seats):
        prev = -1
        max_dist = 0

        for i, seat in enumerate(seats):
            if seat == 1:
                if prev == -1:
                    # Leading empty seats
                    max_dist = i
                else:
                    # Middle gap, sit in the middle
                    max_dist = max(max_dist, (i - prev) // 2)
                prev = i

        # Trailing empty seats
        max_dist = max(max_dist, len(seats) - 1 - prev)

        return max_dist
