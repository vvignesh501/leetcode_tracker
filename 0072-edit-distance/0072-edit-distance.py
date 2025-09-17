class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        # https://www.youtube.com/watch?v=XYi2-LPrwm4&t=465s
        # Create dp table with an extra row and col (len(word) + 1)
        # Extra row and col for scenario where word2 = "" word1 = "abc" it takes 3 operations to fill word1
        
        dp = [[0 for _ in range(len(word2) + 1)]for _ in range(len(word1) + 1)]

        r = len(word1)
        c = len(word2)

        # hence 3, 2, 1, 0 for last empty row
        for i in range(r + 1):
            dp[i][c] = r - i

        # hence 3, 2, 1, 0 for last empty col
        for j in range(c + 1):
            dp[r][j] = c - j

        # Fill the rem dp table, down approach
        for i in range(r -1, -1, -1):
            for j in range(c - 1, -1, -1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    # Insert dp[i +1][j], delete - dp[i][j + 1], replace - dp[i + 1][j + 1]
                    # We need the minimalistic approach to reach the destination
                    dp[i][j] = 1 + min(dp[i][j + 1], dp[i+1][j], dp[i+1][j+1])
        
        return dp[0][0]

# Time = O(m * n)
# Space = = O(m * n)
