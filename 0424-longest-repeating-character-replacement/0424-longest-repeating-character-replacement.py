class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        l = 0
        r = 0
        res = 0
        maxFreq = {}

        for r in range(len(s)):
            maxFreq[s[r]] = 1 + maxFreq.get(s[r], 0)
            maxVal = max(maxFreq.values())

            while (r - l + 1) - maxVal > k:
                maxFreq[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
            
        return res

# Time Complexity: O(n) (since we only shrink l once per character, 
# and max() is over ≤26 letters → O(1)).
# Space Complexity: O(1) (dictionary size ≤ 26).


        