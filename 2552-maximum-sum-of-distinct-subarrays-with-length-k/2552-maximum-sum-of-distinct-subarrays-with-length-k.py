class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:

        l = 0
        seen = set()
        max_sum = curr_sum = 0

        for r in range(len(nums)):
            
            # Slide the pointer from left until the duplicates are gone
            while nums[r] in seen:
                seen.remove(nums[l])
                curr_sum -= nums[l]
                l += 1

            # Add the curr element until k
            seen.add(nums[r])
            curr_sum += nums[r]

            # When k, find the max sum and slide the left 
            if (r - l) + 1 == k:
                max_sum = max(max_sum, curr_sum)
                seen.remove(nums[l])
                curr_sum -= nums[l]
                l += 1
        
        return max_sum

# Time - O(n) → each element added/removed once
# Space - O(k) → at most k elements in the set
            
        