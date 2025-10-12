class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        l = 0
        min_len = float("inf")
        total = 0

        for r in range(len(nums)):
            total += nums[r]
            
            while total >= target:
                min_len = min(min_len, (r - l + 1))
                total -= nums[l]
                l += 1
        
        return min_len if min_len < float("inf") else 0

            


        