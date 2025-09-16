class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        i = 0
        max_profit = 0

        for j in range(1, len(prices)):
            if prices[i] < prices[j]:
                max_profit = max(max_profit, prices[j] - prices[i])
            else:
                i = j
        
        return max_profit

# Time = O(n)
# Space = O(1)

        