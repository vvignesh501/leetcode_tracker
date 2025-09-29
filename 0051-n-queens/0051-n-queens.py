class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        col = set()
        diag = set()
        anti_diag = set()
        res = []
        board = [["."] * n for _ in range(n)]

        def backtracking(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return

            for c in range(n):
                if c in col or (r - c) in diag or (r + c) in anti_diag:
                    continue
                
                board[r][c] = "Q"
                col.add(c)
                diag.add(r - c)
                anti_diag.add(r + c)

                backtracking(r + 1)

                board[r][c] = "."
                col.remove(c)
                diag.remove(r - c)
                anti_diag.remove(r + c)

        backtracking(0)
        return res

# Time - O(n!) (upper bound for N-Queens backtracking)
# Space - O(S.n^2) S = number of valid N-Queens solutions for size n