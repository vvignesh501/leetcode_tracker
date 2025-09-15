class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        # # Using DFS approach - not ideal solution
        # res = []
        # output = []
        # def dfs(res, rem):
        #     if rem == 0:
        #         output.append(len(res))
        #         return 

        #     if rem < 0:
        #         return
            
        #     for coin in coins:
        #         res.append(coin) 
        #         dfs(res, rem - coin)
        #         res.pop()
                
        
        # dfs(res, amount)
        # return min(output) if output else -1
        
        # Dynamic program
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    # 1 here is the current coin. i.e current coin + (i-curr)
                    dp[i] = min(dp[i], dp[i - coin] + 1)

        return dp[amount] if dp[amount] != float("inf") else -1