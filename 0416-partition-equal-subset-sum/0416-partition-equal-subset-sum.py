class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False

        target = total // 2
        dp = {0}  # possible sums starting with 0

        for num in nums:
            nextDP = set(dp)  # carry over previous sums
            for t in dp:
                if t + num == target:
                    return True
                if t + num < target:
                    nextDP.add(t + num)
            dp = nextDP

        return target in dp

# Time: O(n * target) where target = sum(nums)/2
# Space: O(target)
                