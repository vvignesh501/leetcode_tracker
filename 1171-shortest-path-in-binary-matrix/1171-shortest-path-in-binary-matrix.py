class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        n = len(grid)
        if grid[0][0] != 0 or grid[n-1][n-1] != 0:
            return -1
        
        queue = deque([(1, 0, 0)]) if grid[0][0] == 0 else deque()
        directions = [(-1,-1), (-1,0), (-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

        dist = 0
        visited = set()
        visited.add((0, 0))
        while queue:
            dist, r, c = queue.popleft()

            # Return immediately when reaching bottom-right
            if r == n-1 and c == n-1:
                return dist

            for row, col in directions:
                rr, cc = row + r, col + c
                if 0 <= rr < n and 0 <= cc < n and (rr, cc) not in visited and grid[rr][cc] == 0:
                    queue.append((dist + 1, rr, cc))
                    visited.add((rr, cc))
        
        return -1


# Time - O(8⋅n^2)=O(n^2)
# Space Complexity: O(n²)