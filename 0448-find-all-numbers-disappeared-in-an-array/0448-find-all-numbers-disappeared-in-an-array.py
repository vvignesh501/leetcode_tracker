class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        res = []
        for num in nums:
            # -1 converts the 1-based number to 0-based array index.
            # abs(num) ensures we get the original number, ignoring previous markings.
            index = abs(num) - 1
            nums[index] = -abs(nums[index])
        
        for i in range(len(nums)):
            if nums[i] > 0:
                # Because you subtracted -1 above
                res.append(i + 1)
        
        return res


        