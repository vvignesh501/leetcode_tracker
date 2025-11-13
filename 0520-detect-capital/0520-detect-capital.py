class Solution:
    def detectCapitalUse(self, word: str) -> bool:

        if len(word) == 1:
            return True
        
        return word.isupper() or word.islower() or (word[0].isupper() and word[1:].islower())

# Time - O(n)
# Space - O(1)
        