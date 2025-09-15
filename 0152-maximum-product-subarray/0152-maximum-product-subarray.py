class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        min_prod = max_prod = res = nums[0]
        for i in range(1, len(nums)):

            if nums[i] < 0:
                min_prod, max_prod = max_prod, min_prod

            min_prod = min(nums[i], min_prod * nums[i])
            max_prod = max(nums[i], max_prod * nums[i])
            res = max(res, max_prod)

        return res

# Time = O(n)
# Space = O(1)