class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        rows = len(matrix)
        cols = len(matrix[0])

        r, c = set(), set()

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    r.add(i)
                    c.add(j)
        
        for i in range(rows):
            for j in range(cols):
                if i in r or j in c:
                    matrix[i][j] = 0

# Time - O(n^2)
# Space - O(1)