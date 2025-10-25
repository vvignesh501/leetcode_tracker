class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        i = 0

        # i doesn’t move until a new number appears. 
        # It starts at 0 and 1 for the first two elements, 
        # then waits at i = 2 until a different number arrives — only then does i increase again

        # [1,  1,   1,  2]
        #  i=0 i=1  i = 2 -> increment i only when number is different

        for n in nums:
            # For first 2 nums n!= nums[i-2] wont work, hence i < 2
            if i < 2 or n != nums[i - 2]:
                nums[i] = n
                i += 1

        return i

# Time - O(n)
# Space - O(1)