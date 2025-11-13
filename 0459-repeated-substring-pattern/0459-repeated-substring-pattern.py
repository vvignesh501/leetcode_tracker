class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return s in (s + s)[1:-1]


#  Time → O(n)

# Because s in (s+s)[1:-1] runs a substring search in a string of size 2n.

# Space → O(n)

# Because s+s allocates a new string of length 2n.