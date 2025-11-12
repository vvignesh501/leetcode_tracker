class Solution:
    def isPalindrome(self, s: str) -> bool:

        cleaned_s = "".join(c.lower() for c in s if c.isalnum())
        return cleaned_s == cleaned_s[::-1]

# [::--1] doesn't change the original string it creates a copy in another list
# Time - O(n)
# Space - O(n) (for cleaned string