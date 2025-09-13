class Solution:
    def rob(self, nums: List[int]) -> int:

        # f houses are in a circle, and you rob house 0, you can’t rob house n-1.
        # Similarly, if you rob house n-1, you can’t rob house 0.
        # So — you must make a choice:

        # Case 1: Rob from house 0 to n-2
        # You exclude the last house.
        # This behaves just like original House Robber problem.

        # Case 2: Rob from house 1 to n-1
        # You exclude the first house.

        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        def rob_circular(nums):
            n = len(nums)
            if n == 0:
                return 0
            if n == 1:
                return nums[0]

            dp = [0] * n
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])

            for i in range(2, n):
                dp[i] = max(dp[i-1], dp[i-2] + nums[i])

            return dp[n-1]

        return max(rob_circular(nums[:-1]), rob_circular(nums[1:]))

# Time = O(n)
# Space = O(n)
