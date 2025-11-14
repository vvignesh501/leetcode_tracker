class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set('aeiouAEIOU')
        s = list(s)  # Convert string to list to modify it

        left, right = 0, len(s) - 1

        while left < right:
            # Move left pointer forward until it hits a vowel
            while left < right and s[left] not in vowels:
                left += 1
            # Move right pointer backward until it hits a vowel
            while left < right and s[right] not in vowels:
                right -= 1
            
            # Swap vowels
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

        return ''.join(s)

# Time - O(n)
# Space - O(1) but its O(v) as vowels sets are stored
# The vowel set is constant size (always 10 chars → O(1)).