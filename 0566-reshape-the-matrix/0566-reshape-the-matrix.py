class Solution:
    def matrixReshape(self, mat, r, c):
        m, n = len(mat), len(mat[0])
        if m * n != r * c:
            return mat  # can't reshape

        flat = [num for row in mat for num in row]
        new_mat = []

        # A flattened 1D list containing all elements of the matrix in row order.
        # We want to reshape it into rows, each containing exactly c columns.
        for i in range(0, len(flat), c):
            new_mat.append(flat[i:i + c])
        return new_mat

# Time: O(m × n)
# Space: O(m × n) (for new matrix)