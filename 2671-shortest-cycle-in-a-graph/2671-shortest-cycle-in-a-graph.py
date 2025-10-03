from collections import defaultdict, deque

class Solution:
    def findShortestCycle(self, n: int, edges: list[list[int]]) -> int:
        # Build adjacency list
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        min_cycle = float("inf")

        # BFS from every node
        for start in range(n):
            dist = [float("inf")] * n   # distance from start node
            parent = [-1] * n           # parent in BFS tree
            dist[start] = 0
            q = deque([start])

            while q:
                node = q.popleft()
                for nei in adj[node]:
                    if dist[nei] == float("inf"):
                        # Not visited yet
                        dist[nei] = dist[node] + 1
                        parent[nei] = node
                        q.append(nei)
                    elif parent[node] != nei:
                        # Back edge found → cycle
                        cycle_len = dist[node] + dist[nei] + 1
                        min_cycle = min(min_cycle, cycle_len)

        return -1 if min_cycle == float("inf") else min_cycle
