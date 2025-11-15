class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        res = [0] * len(nums)
        l = 0
        r = len(nums) - 1
        idx = r

        while l <= r:

            if abs(nums[l]) < abs(nums[r]):
                res[idx] = nums[r] * nums[r]
                r -= 1
            else:
                res[idx] = nums[l] * nums[l]
                l += 1
            idx -= 1
        
        return res

# Time - O(n)
# Space - O(n)