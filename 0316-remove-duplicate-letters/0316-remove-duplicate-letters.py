class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        seen = set()
        last_index = {c: i for i, c in enumerate(s)}

        for i, c in enumerate(s):
            if c in seen:
                continue
            while stack and c < stack[-1] and last_index[stack[-1]] > i:
                seen.remove(stack.pop())
            stack.append(c)
            seen.add(c)
                    
        return "".join(stack)

# Time: O(n)

# Space: O(1) (bounded by alphabet size, otherwise O(k) where k ≤ n).