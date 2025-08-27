class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # Create 3 hashmap - rows only, cols only, and 3*3 grid with rows and cols only
        # While traversing through 2 dimensional array, check if each value in board
        # contains the same value in rows, cols and grid.
        # Note - this problem asks only if the provided nos make a sudoku. 
        # Your job is not to fill the remaining nos.

        rows = len(board)
        cols = len(board[0])
        
        # Note these hashsets are 1 dim not 2 dim like input board
        rowHashSet = collections.defaultdict(set)
        colHashSet = collections.defaultdict(set)
        grid = collections.defaultdict(set)

        for i in range(rows):
            for j in range(cols):
                
                if board[i][j] == ".":
                    continue

                # Check notes above rowHashSet[i] not rowHashSet[i][j]
                if (board[i][j] not in rowHashSet[i] and 
                board[i][j] not in colHashSet[j] and 
                board[i][j] not in grid[(i//3, j//3)]):
                    rowHashSet[i].add(board[i][j])
                    colHashSet[j].add(board[i][j])
                    grid[(i//3, j//3)].add(board[i][j])
                else:
                    return False
        return True

                