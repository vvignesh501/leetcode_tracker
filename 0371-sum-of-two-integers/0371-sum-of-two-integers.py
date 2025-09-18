class Solution:
    def getSum(self, a: int, b: int) -> int:
        # Step 1: XOR does sum without carry
        sum_without_carry = a ^ b
        # Step 2: AND operator does the carry
        carry = (a & b) << 1
        # Step 3: full sum = sum_without_carry + carry
        full_sum = sum_without_carry + carry
        return full_sum

# Time - O(1)
# Space - O(1)