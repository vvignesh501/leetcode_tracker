from typing import List
from collections import defaultdict

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        count = defaultdict(int)
        l = 0
        max_fruits = 0

        for r in range(len(fruits)):
            count[fruits[r]] += 1

            # shrink window if more than 2 types
            while len(count) > 2:
                count[fruits[l]] -= 1
                if count[fruits[l]] == 0:
                    del count[fruits[l]]
                l += 1

            # update max length
            max_fruits = max(max_fruits, r - l + 1)

        return max_fruits
