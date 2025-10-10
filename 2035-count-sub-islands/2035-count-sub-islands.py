class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        rows, cols = len(grid1), len(grid1[0])
        visited = set()

        def dfs(r, c):
            # If out of bounds or water in grid2 → stop
            if not (0 <= r < rows and 0 <= c < cols and grid2[r][c] == 1):
                return True

            grid2[r][c] = 0  # mark as visited
            valid = grid1[r][c] == 1  # Check if same position in grid1 is land

            # Explore all 4 directions
            for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                if not dfs(r + dr, c + dc):
                    valid = False
            return valid

        count = 0
        for r in range(rows):
            for c in range(cols):
                if grid2[r][c] == 1 and dfs(r, c):
                    count += 1

        return count


# Time Complexity

# O(m × n) → every cell visited once.

# \U0001f4be Space Complexity

# O(m × n) recursion (DFS stack in worst case).
