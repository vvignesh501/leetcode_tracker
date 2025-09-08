class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        if not grid:
            return 0

        def dfs(r, c, count):

            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] == 0:
                return 

            # count[0] because count is immutable, cannot be accessed
            # outside the function, hence create a list
            if grid[r][c] == 1:
                count[0] += 1
                
            # DFS and mark 4 directions as 0 i.e visited
            grid[r][c] = 0

            dfs(r + 1, c, count)
            dfs(r, c + 1, count)
            dfs(r - 1, c, count)
            dfs(r, c - 1, count)
            
        max_area = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    count = [0] # mutable counter
                    dfs(r, c, count)
                    max_area = max(max_area, count[0])

        return max_area

# Wrong
# Time = O(m * n * 4 ^N) 
# Space = O(1)

# Correct - because So even if DFS explores 4 directions recursively, 
# every land cell is visited only once. 
# That’s why the total time is O(rows × cols).
# Time  = O(m * n)
# Space = O(m * n)  