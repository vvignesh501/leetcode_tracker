class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        res = [0] * len(nums)
        l = 0
        r = len(nums) - 1
        idx = r

        while l <= r:

            if abs(nums[l]) < abs(nums[r]):
                multiply = nums[r] * nums[r]
                res[idx] = multiply
                idx -= 1
                r -= 1
            else:
                multiply = nums[l] * nums[l]
                res[idx] = multiply
                idx -= 1
                l += 1
        
        return res
        