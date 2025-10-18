class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        # A simple cycle - find the largest element thing
        # Since mentioned as slope - it can be considered as binary search
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid
        
        return left

# Time - O(n)
# Space - O(1)