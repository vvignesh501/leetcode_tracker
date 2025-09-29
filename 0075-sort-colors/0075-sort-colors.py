class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # Can be sorted in linear time O(n) using bucket sort instead of usual sort O(nlogn)
        # Use the left, right and the current index logic
        
        l, r = 0, len(nums) - 1
        i = 0
        
        def swap(i, j):
            nums[i], nums[j] = nums[j], nums[i]
        
        while i <= r:
            
            if nums[i] == 0:
                swap(l, i)
                l += 1
            
            elif nums[i] == 2:
                swap(i, r)
                r -= 1
                # Decrement i here because to negate the increament outside
                # we decrement here
                i -= 1
            i += 1