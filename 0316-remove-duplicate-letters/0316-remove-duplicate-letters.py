class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        seen = set()
        last_index = {c: i for i, c in enumerate(s)}

        for i, c in enumerate(s):
            if c in seen:
                continue
            
            # last_index[stack[-1]] says whether the same character come again in s, or this
            # is the end. Eg: bcabc -> when i is at b (i=0, 3) i=0 last_index[b] = 3
            while stack and c < stack[-1] and i < last_index[stack[-1]]:
                seen.remove(stack.pop())
            stack.append(c)
            seen.add(c)
                    
        return "".join(stack)

# Time: O(n)

# Space: O(1) (bounded by alphabet size, otherwise O(k) where k ≤ n).