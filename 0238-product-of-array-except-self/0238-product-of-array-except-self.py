class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prefix = [1] * len(nums)
        postfix = [1] * len(nums)
        result = []

        # Prefix runs for all except 0
        # Calculate the previous while doing greedy approach
        for i in range(1, len(nums)):
            prefix[i] = prefix[i - 1] * nums[i - 1]

        # postfix runs for all except last value
        for i in range(len(nums) - 2, -1, -1):
            postfix[i] = postfix[i + 1] * nums[i + 1]

        print(prefix, postfix)

        # prefix * postfix = result
        for i in range(len(nums)):
            result.append(prefix[i] * postfix[i])
        
        return result
        