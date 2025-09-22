class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n not in seen:
            seen.add(n)
            n = sum(int(i)**2 for i in str(n))
        return n == 1

# Time per iteration: O(log n) (digits of n)

# Space - Number of iterations: O(1) practically
        