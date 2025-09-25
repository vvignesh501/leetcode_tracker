class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:

        stack = []

        # Add cnt to the stack, whenever repeated characters are seen, add to the cnt
        # Pop the entire aaa or bbb when cnt == k
    
        for ch in s:
            if stack and ch == stack[-1][0]:
                stack[-1][1] += 1
                if stack[-1][1] == k:   
                    stack.pop()
            else:
                stack.append([ch, 1])

        # Finally multiply a * a as final stack will be ['a': 2, 'b':3] etc.
        return "".join(ch * cnt for ch, cnt in stack)

# Time - O(n)
# Space - O(n)

        