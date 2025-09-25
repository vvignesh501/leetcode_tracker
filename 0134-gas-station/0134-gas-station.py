class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        if sum(gas) < sum(cost):
            return -1
        
        # Solution - Neetcode (simple and easy) Prblem is hard to understand
        total, res = 0, 0
        for i in range(len(gas)):
            total += gas[i] - cost[i]

            if total < 0:
                total = 0
                # At the last reset (i=2), we set res=3.
                # Then we finish the loop without resetting again.
                # So the answer stays at 3 — it doesn’t get bumped to 4.
                # The first positive value after -ve is the result
                res = i + 1
        
        return res

# Time - O(n)
# Space - O(1)