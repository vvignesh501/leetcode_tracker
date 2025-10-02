import heapq
from collections import defaultdict

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float],
                       start_node: int, end_node: int) -> float:
        adj = defaultdict(list)
        for (a, b), prob in zip(edges, succProb):
            adj[a].append((b, prob))
            adj[b].append((a, prob))

        # Max heap: (-probability, node)
        heap = [(-1.0, start_node)]
        probs = [0.0] * n
        probs[start_node] = 1.0

        while heap:
            curr_prob, node = heapq.heappop(heap)
            curr_prob = -curr_prob  # Convert back to positive

            # If we reached end, return the probability
            if node == end_node:
                return curr_prob

            # Explore neighbors
            for nei, edge_prob in adj[node]:
                new_prob = curr_prob * edge_prob
                if new_prob > probs[nei]:
                    probs[nei] = new_prob
                    heapq.heappush(heap, (-new_prob, nei))

        return 0.0

# Time - O(Edges * log Node) - The vertices (or nodes) are heappush or heappop i.e logn
# Space - O(V + E) because of adjList