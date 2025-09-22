class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        N = len(matrix)
        
        for r in range(N):
            for c in range(r):

                # Row 0, column 1 becomes row 1 column 0 after swap
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
                print(matrix)
        
        # Every row is a list in matrix, reverse the list.
        # Reverse is used because it reverses in place.
        for r in matrix:
            r.reverse()

# Time - O(n^2)
# Space - O(1)