class Solution:
    def reverseWords(self, s: str) -> str:
        
        res = []
        split_word = s.split()
        for word in split_word:
            res.append(word[::-1])
        
        return ' '.join(res)