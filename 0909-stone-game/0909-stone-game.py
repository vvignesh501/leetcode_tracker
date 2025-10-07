class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        dp = {}

        def dfs(l, r):
            # Base case: one pile left
            if l == r:
                return piles[l]

            if (l, r) in dp:
                return dp[(l, r)]

            # Alice tries to maximize her lead
            # dp[l][r] = max(piles[l] - dp[l+1][r], piles[r] - dp[l][r-1])
            dp[(l, r)] = max(piles[l] - dfs(l + 1, r),
                             piles[r] - dfs(l, r - 1))
            return dp[(l, r)]

        # If Alice’s score difference is positive, she wins
        return dfs(0, n - 1) > 0

# Time - O(n^2)
# Space - O(n)