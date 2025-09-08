class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        if not grid:
            return 0

        def dfs(r, c):

            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] == '0':
                return 
                
            # DFS and mark 4 directions as 0 i.e visited
            grid[r][c] = '0'

            dfs(r + 1, c)
            dfs(r, c + 1)
            dfs(r - 1, c)
            dfs(r, c - 1)
            
        count = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1':
                    count += 1
                    dfs(r, c)
        
        return count

     # Time O(R × C)
     # Space O(R × C)   