class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        l = 0
        r = 0
        substring = set()
        maxTotal = 0

        while l < len(s) and r < len(s):
            if s[r] not in substring:
                substring.add(s[r])
                r += 1
                maxTotal = max(maxTotal, len(substring))  # move maxTotal update here
            else:
                substring.remove(s[l])
                l += 1
        
        return maxTotal

# Time complexity = O(n)
# Space = O(n)