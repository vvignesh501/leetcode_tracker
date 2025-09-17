class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        l = 0
        r = 0
        max_subarray = nums[0]
        sum_ = nums[0]

        while l < len(nums) - 1:
            if sum_< 0:
                l += 1
                sum_ = nums[l]
            else:
                l += 1
                sum_ += nums[l]
            max_subarray = max(max_subarray, sum_)
        
        return max_subarray

# Time = O(n)
# Space = O(1)