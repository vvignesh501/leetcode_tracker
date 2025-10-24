# class Solution:
#     def missingNumber(self, nums: List[int]) -> int:

#         n = len(nums)
#         xor = 0

#         # Create a xor array from 0,1,2,3
#         for i in range(n + 1):
#             xor = xor ^ i

#         # Now xor with original nums array.
#         # XORing basically cancells the duplicates i.e ones 
#         # the nums existing & keeps only the missing number
#         # thats how xor works

#         for num in nums:
#             xor = xor ^ num

#         return xor
        
# Time - O(n)
# Space - O(1)


# Formula - Missing number from a series of consecutive integers (1 to N) 
# Formula: (Missing Number=(N(N+1)}\2) - Sum of the given numbers

class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        n = len(nums)
        missing = (n * (n + 1)//2) - sum(nums)
        return missing