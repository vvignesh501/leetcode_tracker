import heapq
from typing import List

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        # Build adjacency list
        adj = {i: [] for i in range(n)}
        for u, v, w in flights:
            adj[u].append((v, w))
        
        # MinHeap: (cost_so_far, node, stops_remaining)
        heap = [(0, src, k + 1)]
        
        # Track the best stops remaining for each node with a given cost
        best = dict()  # key = (node), value = max stops remaining
        
        while heap:
            cost, node, stops = heapq.heappop(heap)
            
            # If destination, return cost
            if node == dst:
                return cost
            
            # Skip if we already visited node with >= remaining stops
            if node in best and best[node] >= stops:
                continue
            
            best[node] = stops
            
            # Explore neighbors if we have stops left
            if stops > 0:
                for nei, price in adj[node]:
                    heapq.heappush(heap, (cost + price, nei, stops - 1))
        
        return -1
