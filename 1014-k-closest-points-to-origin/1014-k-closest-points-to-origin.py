class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        res = []
        minHeap = []
        for x, y in points:
            # d = sqrt(x^2 + y^2) or d^2 = x^2 + y^2
            # No need to perform sqrt as you do sqrt for all x and y in points, it gives
            # still the same answer

            # distance formula - (sqrt((x1 - x2)^2 + (y1 - y2)^2)).
            # This applies for distanc between two points, but for distanc between one 
            # point to the origin (0, 0) is sqrt(x1-0)^2 + (y1 -0)^2
            dist = (x**2 + y**2)
            minHeap.append([dist, x, y])
        
        heapq.heapify(minHeap)
        
        while k >= 1:
            dist, x, y = heapq.heappop(minHeap)
            res.append([x, y])
            k -= 1
        return res

# Time - O(n log n)
# Space - O(n)