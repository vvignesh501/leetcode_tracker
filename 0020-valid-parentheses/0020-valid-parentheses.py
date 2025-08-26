class Solution:
    def isValid(self, s: str) -> bool:

        brackets = {"(": ")", "{": "}", "[": "]"}
        stack = []

        for ch in s:
            if ch in brackets:
                stack.append(ch)
            else:
                if not stack:
                    return False
                opening_bracket = stack.pop()
                if brackets[opening_bracket] != ch:
                    return False
        return len(stack) == 0

        