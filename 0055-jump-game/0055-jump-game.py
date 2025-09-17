class Solution:
    def canJump(self, nums: List[int]) -> bool:

        m = len(nums)-1
        goal = m
        for i in range(m, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        
        return True if goal == 0 else False

# Time = O(n)
# Space = O(1)
        