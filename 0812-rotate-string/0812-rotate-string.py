class Solution:
    def rotateString(self, s: str, goal: str) -> bool:

        # Move the leftmost character of s to the rightmost position
        return len(s) == len(goal) and goal in s + s

# Time - O(2n) - O(n) for concatenation + O(n) for substring search → O(n) overall.
# Space - O(n) as it saves s + s in memory