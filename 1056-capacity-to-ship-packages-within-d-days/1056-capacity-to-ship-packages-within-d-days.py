class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        left = max(weights)
        right = sum(weights)

        def feasible(curr_weight):
            curr_day = 1
            total = 0
            for w in weights:
                if total + w <= curr_weight:
                    total += w
                else:
                    curr_day += 1       # start new day
                    total = w           # start new day with current package
                    if curr_day > days:
                        return False
            return True



        # Perform binary search - find the mid of the weight capacity and see for results and so on.
        while left <= right:
            mid = (left + right) // 2

            if feasible(mid):
                right = mid - 1
            else:
                 left = mid + 1
        return left

        