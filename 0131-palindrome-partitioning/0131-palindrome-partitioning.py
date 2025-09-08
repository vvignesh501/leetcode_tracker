class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []

        def is_palindrome(sub):
            return sub == sub[::-1]

        def backtrack(start, path):
            if start == len(s):          # Reached the end
                result.append(path.copy())
                return
            
            for end in range(start + 1, len(s) + 1):
                substring = s[start:end]
                if is_palindrome(substring):
                    path.append(substring)
                    backtrack(end, path)  # Recurse for remaining string
                    path.pop()            # Backtrack

        backtrack(0, [])
        return result


# Time - O(n * 2 **n) - 2 **n = 2 choices in dfs
# Space - O(n)