class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        # Do not see the example - its very confusing
        # Just the remove the element and place the other element in place but replace
        # on the index, where the element was removed

        l = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[l] = nums[i]
                l += 1

        return l        