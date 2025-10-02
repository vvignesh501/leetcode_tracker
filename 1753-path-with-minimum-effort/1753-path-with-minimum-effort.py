class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        
        queue = [(0, 0, 0)]
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        visited = set()

        while queue:
            # Heap queue takes care of the min effort needed by choosing the min value
            diff, row, col = heapq.heappop(queue)

            if (row, col) in visited:
                continue

            visited.add((row, col))

            # if its the end of the matrix grid
            if (row, col) == (len(heights) - 1, len(heights[0]) - 1):
                return diff

            for rr, cc in directions:
                    newR, newC = rr + row, cc + col
                    if 0 <= newR < len(heights) and 0<= newC < len(heights[0]) and (newR, newC) not in visited:
                        new_diff = abs(heights[row][col] - heights[newR][newC])
                        max_diff = max(new_diff, diff)
                        heapq.heappush(queue, (max_diff, newR, newC))

        return diff