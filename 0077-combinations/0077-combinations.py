class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        result = []
        # Combinations backtracking
        def backtracking(i, output):
            if len(output) == k:
                return result.append(output.copy())
            
            for j in range(i, n + 1):
                output.append(j)
                backtracking(j + 1, output)
                output.pop()

        backtracking(1, output=[])
        return result