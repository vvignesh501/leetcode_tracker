class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        best_left = values[0] + 0   # best value[i] + i seen so far
        best_score = 0

        for j in range(1, len(values)):
            best_score = max(best_score, best_left + values[j] - j)
            best_left = max(best_left, values[j] + j)  # update for next j

        return best_score

# Time - O(n)
# Space - O(1)