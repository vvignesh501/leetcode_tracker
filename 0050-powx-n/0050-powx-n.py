class Solution:
    def myPow(self, x: float, n: int) -> float:

        def pow(x, n):

            # Base case
            if x == 0: return 0
            if n == 0: return 1

            res = pow(x, n //2)
            res = res * res
            return x * res if n % 2 == 1 else res
        
        res = pow(x, abs(n))
        return res if n >= 0 else 1/res


# Time: O(logn) — each step halves n

# Space:

# Recursive: O(log n) call stack

# Iterative: O(1)