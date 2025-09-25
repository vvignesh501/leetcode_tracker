class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        island_size = {}
        island_id = 2  # start from 2 to mark islands uniquely
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]
        
        def dfs(r, c, id_):
            size = 1
            grid[r][c] = id_
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 1:
                    size += dfs(nr, nc, id_)
            return size
        
        # 1. Label islands and record their sizes
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    size = dfs(r, c, island_id)
                    island_size[island_id] = size
                    island_id += 1

        # Edge case: if no 0, return whole grid
        if not any(0 in row for row in grid):
            return n * n
        
        max_area = 0
        
        # 2. Try flipping each 0 and calculate new island size
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 0:
                    seen = set()
                    area = 1
                    for dr, dc in dirs:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] > 1:
                            id_ = grid[nr][nc]
                            if id_ not in seen:
                                area += island_size[id_]
                                seen.add(id_)
                    max_area = max(max_area, area)
        
        return max_area

# Time - Total = O(n²)
# Space - Total = O(n²)