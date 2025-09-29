class Solution:
    def sortColors(self, nums: List[int]) -> None:

        # l = next position for 0, r = next position for 2
        l, r = 0, len(nums) - 1  
        i = 0   # current index

        def swap(x, y):
            nums[x], nums[y] = nums[y], nums[x]

        # Process each element until current index passes r
        while i <= r:
            if nums[i] == 0:
                # Place 0 at the next left position
                swap(l, i)   # safe even if i == l (self-swap)
                l += 1
                i += 1       # move to next element
            elif nums[i] == 2:
                # Place 2 at the next right position
                swap(i, r)
                r -= 1
                # Do NOT increment i here, because the new nums[i] needs to be checked
            else:
                # nums[i] == 1, already in the middle
                i += 1
            
        

# Time - O(n)
# Space - O(1)