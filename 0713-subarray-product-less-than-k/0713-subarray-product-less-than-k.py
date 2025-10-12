class Solution:
    def numSubarrayProductLessThanK(self, nums, k):
        l, r = 0, 0
        out = 0
        product = 1
        
        for r in range(len(nums)):
            product *= nums[r]

            # Decrement the window from left until the product becomes < k again
            while l <= r and product >= k:
                product /= nums[l]
                l += 1
            out += r - l + 1
        return out

# Time - O(n)
# Space - O(1)