class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if not digits:
            return []

        digit_to_letters = {
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
        def backtracking(idx, comb):
            
            if idx == len(digits):
                result.append(comb[:])
                return

            for letter in digit_to_letters[digits[idx]]:
                backtracking(idx + 1, comb + letter)

        
        backtracking(0, "")        
        return result



        