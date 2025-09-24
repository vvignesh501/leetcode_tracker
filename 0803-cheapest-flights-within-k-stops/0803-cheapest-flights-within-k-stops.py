from typing import List

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # costs[i] = cheapest cost to reach node i with <= current #stops
        prices = [float("inf")] * n
        prices[src] = 0

        # Relax edges at most (k+1) times (because k stops = k+1 edges)
        # Create two list - prices and tmpPrices. Make all changes to tmpPrices
        # and move it to prices. Do it until K + 1 is Bellman ford algo.

        for _ in range(k + 1):
            tmpPrices = prices.copy()
            for u, v, p in flights:
                if prices[u] == float('inf'):
                    continue
                if prices[u] + p < tmpPrices[v]:
                    tmpPrices[v] = prices[u] + p
            prices = tmpPrices

        return -1 if prices[dst] == float('inf') else prices[dst]

# Time Complexity:
# Outer loop runs (k+1) times.
# Inner loop scans all m = len(flights) edges.
# → O(k · m)

# Space Complexity:

# costs and new_costs arrays → O(n)

# Input adjacency list (flights) → O(m)
# → Overall O(n + m), often simplified to O(n) if we only count the DP arrays.
