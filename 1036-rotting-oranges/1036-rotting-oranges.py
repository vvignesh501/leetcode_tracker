class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        rows = len(grid)
        cols = len(grid[0])
        fresh = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        minutes = 0
        while q and fresh > 0:
            for _ in range(len(q)):
                r, c = q.popleft()
                directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
                for rr, rc in directions:
                    newR, newC = rr + r, rc + c
                    if newR >= 0 and newR < rows and newC >= 0 and newC < cols and grid[newR][newC] == 1:
                        grid[newR][newC] = 2
                        q.append((newR, newC))
                        fresh -=1 
            minutes += 1
        
        # fresh is needed for return -1, else no other way to track fresh 
        return minutes if fresh == 0 else -1