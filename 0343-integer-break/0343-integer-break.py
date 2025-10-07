class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[1] = 1

        for i in range(2, n + 1):
            for j in range(1, i):
                dp[i] = max(dp[i], j * (i - j), j * dp[i - j])

        return dp[n]

# Metric	Complexity	Why
# Time	O(n²)	For each i, you loop over all j from 1 to i-1
# Space	O(n)	1D DP array of size n+1