from typing import List

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        i, j = 0, len(people) - 1
        boats = 0
        
        while i <= j:
            if people[i] + people[j] <= limit:
                i += 1  # lightest person goes with heaviest
            j -= 1  # heaviest person always goes
            boats += 1
        
        return boats

# Time - O(n)
# Space - O(1)