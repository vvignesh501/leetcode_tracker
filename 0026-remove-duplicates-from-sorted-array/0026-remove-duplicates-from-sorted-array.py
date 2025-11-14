class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return 1


        # Remember eg - [1, 1, 2] start index 1 to len(nums)
        # When index = 1 and index 2 is not same, swap index[2] to index[1]
        # But index[1] has to be incremented before swapping, because i gets incremented only nums are different
        i = 0
        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                i += 1
                # swap nums[j] = 2 to index 1 then, [1, 1, 2] becomes [1, 2]
                nums[i] = nums[j]
            print(nums[i], nums[j])
        return i + 1

# Time - O(n)
# Space - O(1)