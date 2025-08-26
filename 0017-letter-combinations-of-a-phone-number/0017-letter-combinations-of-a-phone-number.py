class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if not digits:
            return []

        phone_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }

        result = []
        def backtracking(index, path):
            if index == len(digits):
                result.append("".join(path))
                return
            
            for char in phone_map[digits[index]]:
                path.append(char)
                backtracking(index + 1, path)
                path.pop()  # undo choice

        
        backtracking(0, [])        
        return result


# Time - O(4ⁿ · n)
# Space - O(n + 4ⁿ)
        