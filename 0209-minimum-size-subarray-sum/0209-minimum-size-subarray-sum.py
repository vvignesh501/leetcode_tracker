class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        l = 0
        min_len = float("inf")
        total = 0

        for r in range(len(nums)):
            total += nums[r]
            
            # shrink the left window until total >= target
            while total >= target:
                min_len = min(min_len, (r - l + 1))
                total -= nums[l]
                l += 1
        
        return min_len if min_len < float("inf") else 0

            
# Time Complexity: O(n)

# Each element is added once and removed once from current_sum.

# So the total number of operations is proportional to 2n.

# Space Complexity: O(1)

# We only use a few variables (left, current_sum, min_len) regardless of the array size. 