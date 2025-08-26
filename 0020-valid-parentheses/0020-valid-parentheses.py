class Solution:
    def isValid(self, s: str) -> bool:

        brackets = {"(": ")", "{": "}", "[": "]"}
        stack = []

        for ch in s:
            # Append when opening bracket
            if ch in brackets:
                stack.append(ch)
            # when ch == closing bracket, 
            # pop the stack and check if opening has a closing bracket
            else:
                if not stack:
                    return False
                opening_bracket = stack.pop()
                if brackets[opening_bracket] != ch:
                    return False
        return len(stack) == 0


# Time = O(n)
# Space = O(n)
        