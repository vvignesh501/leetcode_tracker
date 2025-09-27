class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        graph = defaultdict(dict)
        for (u, v), values in zip(equations, values):
            # left = neighbour, right = value
            graph[u][v] = values
            graph[v][u] = 1/values
        
        def dfs(nei, target, product):
            if nei == target:
                return product

            # left, right added above is used here
            # graph = {'a' :{'b':2}}
            # a = q1, b = neightbour c = value
            for neighbour, val in graph[nei].items():
                if neighbour not in visited:
                    visited.add(neighbour)
                    res = dfs(neighbour, target, val * product)
                    if res != -1.0:
                        return res
            return -1.0

        res = []
        for q1, q2 in queries:
            if q1 not in graph or q2 not in graph:
                res.append(-1.0)
            elif q1 == q2:
                res.append(1.0)
            else:
                visited = set()
                res.append(dfs(q1, q2, 1.0))
        
        return res

# Time = O(Q.E)
# Space ≈ O(E)O(E)O(E)
