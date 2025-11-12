class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        for i in range(len(haystack)):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1
        
# Time - O(n·m)	Each starting position of n length checks up to m characters
# Space	O(1)	Only uses constant extra memory