import heapq

class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        n = len(points)
        visited = set()
        minHeap = [(0, 0)]  # (cost, pointIndex)
        totalCost = 0

        while len(visited) < n:
            cost, i = heapq.heappop(minHeap)
            if i in visited:
                continue
            totalCost += cost
            visited.add(i)

            # push neighbors
            for j in range(n):
                if j not in visited:
                    x1, y1 = points[i]
                    x2, y2 = points[j]
                    dist = abs(x1 - x2) + abs(y1 - y2)
                    heapq.heappush(minHeap, (dist, j))

        return totalCost

# Time: Worst case O(n² log n) because for each of n nodes we push up to n edges into the heap.

# Space: O(n²) heap in worst case.