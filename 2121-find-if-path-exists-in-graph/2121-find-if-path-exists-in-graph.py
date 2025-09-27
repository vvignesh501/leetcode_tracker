class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        graph = defaultdict(list)
        visited = set()

        for e1, e2 in edges:
            graph[e1].append(e2)
            graph[e2].append(e1)

        def dfs(src):
            if src == destination:
                return True

            visited.add(src)
            for node in graph[src]:
                if node not in visited:
                    visited.add(node)
                    if dfs(node):
                        return True
            return False
        
        return dfs(source)
                
# Time - O(n+e)
# Space - O(n+e)