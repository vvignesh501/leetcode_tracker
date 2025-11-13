class Solution:
    def reverseWords(self, s: str) -> str:
        
        res = []
        split_word = s.split()
        
        return " ".join(word[::-1] for word in split_word)

# Time - O(n)
# Space - O(1)