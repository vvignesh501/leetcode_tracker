class Solution:
    def removeKdigits(self, num: str, k: int) -> str:

        if k > len(num):
            return "0"

        # Create a stack whatever stack[-1] > current ch, 
        # pop from stack and append the curr ch
        stack = []
        for ch in num:
            
            while stack and stack[-1] > ch and k >0:
                k -=1
                stack.pop()

            stack.append(ch)

        if k > 0:
            stack = stack[:-k]  # remove last k digits

        # Remove any predecessor zeros when 0200 not when 0
        res = "".join(stack).lstrip("0")
        
        return res if res else "0"

# Time - O(n)
# Space - O(n)
        
        