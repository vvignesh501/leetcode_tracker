class Solution:
    def checkValidString(self, s: str) -> bool:
        low = high = 0
        for ch in s:
            if ch == '(':
                low += 1
                high += 1
            elif ch == ')':
                low -= 1
                high -= 1
            else:  # '*'
                low -= 1   # treat as ')'
                high += 1  # treat as '('
            
            if high < 0:  # too many ')'
                return False
            if low < 0:   # clamp
                low = 0
        return low == 0

# Time: O(n) → one pass

# Space: O(1) → just two counters