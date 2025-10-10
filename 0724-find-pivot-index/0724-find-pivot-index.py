class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
     
        left = 0
        right = sum(nums)
        for i, val in enumerate(nums):
            right -= val
            if left == right:
                return i
            left += val
            
        return -1


        