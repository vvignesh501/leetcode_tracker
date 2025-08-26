class Solution:
    def reverse(self, x: int) -> int:

        abs_x = abs(x)
        reverse = 0
        while abs_x > 0:
            rem = abs_x % 10
            abs_x = abs_x // 10
            reverse = reverse * 10 + rem

        if -2**31 < reverse > 2**31 -1:
            return 0

        return reverse if x > 0 else -reverse

# Time = O(logn) - because the number gets shrunk everytime.
# Space = O(1)

        