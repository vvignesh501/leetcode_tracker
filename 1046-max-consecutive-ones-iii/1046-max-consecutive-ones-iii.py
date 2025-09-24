from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        zeros = 0
        res = 0

        for r in range(len(nums)):
            if nums[r] == 0:
                zeros += 1

            # shrink window if zeros exceed k
            while zeros > k:
                if nums[l] == 0:
                    zeros -= 1
                l += 1

            res = max(res, r - l + 1)

        return res

# Time - O(n) Total operations ≤ 2n → O(n).
# Space - O(1)