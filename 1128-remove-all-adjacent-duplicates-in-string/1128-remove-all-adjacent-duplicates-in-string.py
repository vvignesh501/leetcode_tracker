class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for char in s:
            if stack and char == stack[-1]:
                stack.pop()
            else:
                stack.append(char)
        
        return ''.join(stack)


# Time: O(n) → each char pushed/popped at most once

# Space: O(n) → stack stores at most n characters