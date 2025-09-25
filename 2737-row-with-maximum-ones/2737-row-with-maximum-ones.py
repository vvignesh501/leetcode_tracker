class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:

        max_count = 0
        row_index = 0

        for i, row in enumerate(mat):
            count = sum(row)
            if count > max_count:
                max_count = count
                row_index = i
        
        return [row_index, max_count]

# Time - O(n * m)
# Space - O(1)

        