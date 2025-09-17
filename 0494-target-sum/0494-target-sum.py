from functools import lru_cache

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        @lru_cache(None)
        def dfs(i, total):
            if i == len(nums):
                if total == target:
                    return 1
                else:
                    return 0
            
            return dfs(i + 1, total + nums[i]) + dfs(i + 1, total - nums[i])

        return dfs(0, 0)

# Time: O(2^n) → every number has 2 choices

# Space: O(n) recursion depth