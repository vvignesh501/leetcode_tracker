class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return

        rows, cols = len(board), len(board[0])

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != "O":
                return
            board[r][c] = "T"   # mark safe
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # Step 1: mark border-connected O’s as "T"
        for r in range(rows):
            dfs(r, 0)
            dfs(r, cols - 1)
        for c in range(cols):
            dfs(0, c)
            dfs(rows - 1, c)

        # Step 2: flip all remaining O → X, and T → O
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"


# Time: O(m × n) — every cell is visited at most once.
# Space: O(m × n) worst case recursion stack (or queue