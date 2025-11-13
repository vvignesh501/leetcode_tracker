class Solution:
    def decodeString(self, s: str) -> str:

        stack = []
        curr_str = ""
        curr_num = 0 

        for ch in s:

            # Case 1 - int can be double digits
            if ch.isdigit():
                curr_num = curr_num * 10 + int(ch)

            # Case - append stack as [char, k]
            elif ch == '[':
                stack.append((curr_str, curr_num))
                # reset back curr_str, curr_num
                curr_str = ""
                curr_num = 0

            # Case - when ] multiply the curr_str with curr_num
            elif ch == ']':
                prev_str, digit = stack.pop()
                curr_str = prev_str + digit * curr_str
            
            # Case4 - when its not a digit or [ or ]
            else:
                curr_str += ch
        
        return curr_str

 # Time - O(n)
 # Space - O(n) curr_num and curr_str stores both the string and digit from input       
        