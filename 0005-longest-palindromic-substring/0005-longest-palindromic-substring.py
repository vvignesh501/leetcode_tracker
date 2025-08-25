class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        longestSubstring = ""
        # Do the palindrome logic
        def palindrome(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l + 1:r]
            # Make sure you return the substring
        
        # Call the palindrome function for odd and even
        for i in range(len(s)):
            odd = palindrome(i, i)
            even = palindrome(i, i + 1)

            longestSubstring = max(longestSubstring, odd, even, key=len)
        
        return longestSubstring

        