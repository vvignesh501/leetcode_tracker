class Solution:
    def longestPalindrome(self, s: str) -> str:

        longest_substring = ""
        def expand(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l+1:r]
        
        for i in range(len(s)):
            odd = expand(i, i)
            even = expand(i, i + 1)
            longest_substring = max(longest_substring, odd, even, key=len)
        
        return longest_substring

# Time = O(n**2)
# Space = O(1)

        