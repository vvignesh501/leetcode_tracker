class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        row = len(obstacleGrid) 
        col = len(obstacleGrid[0])   
        dp = [0] * col
        dp[col - 1] = 1

        # Bottom up approach with only one DP in memory needed.
        # Trick here is you don't need 2 dimensions for dp in memory
        for r in range(row - 1, -1, -1):
            for c in range(col - 1, -1, -1):
                if obstacleGrid[r][c]:
                    dp[c] = 0
                elif c + 1 < col:
                    dp[c] = dp[c] + dp[c + 1]
        return dp[0]

# Time - O(n^2)
# Space - O(n)