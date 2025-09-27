from collections import defaultdict

class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        graph = defaultdict(list)
        
        def dfs(src, target, visited):
            if src == target:
                return True
            visited.add(src)
            for neighbor in graph[src]:
                if neighbor not in visited:
                    if dfs(neighbor, target, visited):
                        return True
            return False
        
        for u, v in edges:
            visited = set()
            # If there's already a path from u to v, this edge creates a cycle
            if dfs(u, v, visited):
                return [u, v]
            # Otherwise, add the edge to the graph
            graph[u].append(v)
            graph[v].append(u)
