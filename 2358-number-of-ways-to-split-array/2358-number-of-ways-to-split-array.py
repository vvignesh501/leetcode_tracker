class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        
        left = 0
        right = sum(nums)
        res = 0

        for i in range(len(nums) - 1):
            left += nums[i]
            right -= nums[i]

            if left >= right:
                res += 1
        
        return res if res > 0 else 0