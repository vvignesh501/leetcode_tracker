class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:

        total = len(cardPoints)
        total_sum = sum(cardPoints)

        # Edge case: If we need to leave out all but one card, just pick the maximum card
        if k == total:
            return total_sum
        
        # Number of cards to leave out
        to_leave_out = total - k

        # Initial sum of the first (total - k) cards to leave out
        curr_sum = sum(cardPoints[:to_leave_out])

        # Now, slide the window to get the minimum sum of the subarray to leave out
        min_sum_to_leave_out = curr_sum

        for i in range(to_leave_out, total):
            # Slide the window by removing the first element of the window and adding the next element
            curr_sum += cardPoints[i] - cardPoints[i - to_leave_out]
            min_sum_to_leave_out = min(min_sum_to_leave_out, curr_sum)

        # The maximum score is the total sum minus the minimum sum of the subarray we leave out
        return total_sum - min_sum_to_leave_out
