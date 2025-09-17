class Solution:
    def jump(self, nums: List[int]) -> int:

        if len(nums) <= 1:
            return 0

        l = 0
        r = 0
        steps = 0

        while r < len(nums) - 1:
            farthest = max(i + nums[i] for i in range(l, r + 1))
            l = r + 1
            r = farthest
            steps += 1
        
        return steps

# Time: O(n) (one pass)

# Space: O(1)