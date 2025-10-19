class Solution:
    def matrixReshape(self, mat, r, c):
        m, n = len(mat), len(mat[0])
        if m * n != r * c:
            return mat  # can't reshape

        flat = [num for row in mat for num in row]
        new_mat = []
        for i in range(0, len(flat), c):
            new_mat.append(flat[i:i + c])
        return new_mat

# Time - O(n)
# Space - O(1)