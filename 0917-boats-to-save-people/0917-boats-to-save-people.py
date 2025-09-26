class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:

        boat = 0
        i = 0
        j = len(people) - 1

        people.sort()

        if sum(people) <= limit:
            return 1

        while i <= j:
            if people[i] + people[j] <= limit: # lightest person goes with heaviest
                i += 1
            j -=1 # heaviest person always goes
            boat += 1
        return boat

# Time - O(n)
# Space - O(1)
        
        