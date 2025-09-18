class Solution:
    def countBits(self, n: int) -> List[int]:

# Bit Manipulation
# When an integer is given and asked to convert to bits n = 5 5>>1 
# does the job of directly converting the integer to bit and divide by 2.
        res = []
        for num in range(n + 1):
            total = 0
            while num:
                if num % 2 == 1:
                    total += 1
                num = num >> 1
            res.append(total)
        return res

# Time - O(nlogn)
# Space - O(n)