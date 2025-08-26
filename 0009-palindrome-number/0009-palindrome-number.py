class Solution:
    def isPalindrome(self, x: int) -> bool:

        # Negative nos are not palindrome
        if x < 0:
            return False

        # get the reversed number
        reversed_num = 0
        original = x

        while x > 0:
            rem = x % 10
            reversed_num = reversed_num * 10 + rem
            x = x // 10
        
        # return true if reversed and x are same which is palindrome
        return reversed_num == original

        