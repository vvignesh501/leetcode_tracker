class Solution:
    def reverseBits(self, n: int) -> int:

        # n=1101 reversing = 1011
        # Get the last one by modulo, then move the bits to the right
        # then add the 1 to the left and so.

        res = 0
        for _ in range(32):
            # Step 1 - make room for the next bit on the left
            res <<= 1 # make room for bit 0 to the left
            # Step 2 - Now get the last bit
            res |= n & 1
            # Step 3 - move a value from the right
            n >>= 1
        
        return res

# Time - O(1)
# Space - O(1)

        