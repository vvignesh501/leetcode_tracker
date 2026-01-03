class Solution:
    def numSquares(self, n: int) -> int:
        
        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        for target in range(1, n + 1):
            for s in range(1, target + 1):
                square = s * s

                # Base case
                if target - square < 0:
                    break

                dp[target] = min(dp[target], 1 + dp[target-square])
            
        return dp[n]

# NeetcodeIO  
# Time - O(n. sqrt(n))
# Space - O(n)