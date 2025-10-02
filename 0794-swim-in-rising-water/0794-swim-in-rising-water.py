class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        queue = [(grid[0][0], 0, 0)]
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        visited = set()

        while queue:
            time, row, col = heapq.heappop(queue)

            if (row, col) in visited:
                continue
            
            # If reach end of the grid
            if (row, col) == (len(grid) - 1, len(grid[0]) - 1):
                return time
            
            visited.add((row, col))

            for rr, cc in directions:
                newR, newC = rr + row, cc + col
                if 0 <= newR < len(grid) and 0<= newC < len(grid[0]) and (newR, newC) not in visited:
                    heapq.heappush(queue, (max(grid[newR][newC], time), newR, newC))

    
    # Time: O(n² log n)

# Each of n² cells is pushed/popped from heap once.

# Heap operations cost O(log n²) = O(log n).

# Space: O(n²)

# Visited + heap storage.