class Solution:
    def longestPalindrome(self, words: List[str]) -> int:

        count = Counter(words)
        total = 0
        center = 0

        # Take advantage where there are only 2 chars in a word, so you can check word[0] or word[1]
        # Case 1 - when there is lc, check for cl - when matching remove both lc and cl from hash and add to res
        # Case 2 - where there is gg, only 
        
        for word in list(count.keys()):
            reverse = word[::-1]   

            # Case 1 - Check only chars are same
            if word[0] == word[1]:
                pairs = count[word] // 2
                total += pairs * 4
                count[word] -= pairs * 2

                # When only one character is left, keep it in the middle
                if count[word] % 2 == 1:
                    center = 2

            # Case 2 - check for lc, cl
            elif reverse in count:
                pairs = min(count[word], count[reverse])
                total += pairs * 4
                count[reverse] -= pairs
                count[word] -= pairs  
        
        # Case 3 - words = ["cc","ll","xx"] since there are only 2 chars inside a word
        total += center
        
        return total
            
        