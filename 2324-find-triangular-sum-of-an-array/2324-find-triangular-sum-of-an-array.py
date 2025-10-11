class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        
        newNums = []
        while len(nums) != 1:
            for i in range(len(nums) - 1):
                newNums.append((nums[i] + nums[i + 1]) % 10)
            nums = newNums.copy()
            newNums = []
        
        return nums[0]

# Time - O(n^2) using while and for
# Space - Each round creates a new list → O(n)
# Can be reduced to O(1) if done in-place (modifying nums directly).