from functools import lru_cache

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        @lru_cache
        def dfs(i, j):
            if i == len(triangle) - 1:
                return triangle[i][j]

            return triangle[i][j] + min(dfs(i + 1, j), dfs(i + 1, j + 1))
        
        return dfs(0, 0)

# Time - O(n²)
# Space - O(n²)