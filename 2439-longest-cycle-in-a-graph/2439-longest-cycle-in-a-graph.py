class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        n = len(edges)
        visited = [False] * n
        max_cycle = -1  # -1 if no cycle exists

        def dfs(node, depth, seen):
            if node in seen:  # cycle detected
                return depth - seen[node]

            if visited[node] or node == -1:  # already processed or no outgoing edge
                return -1

            seen[node] = depth
            res = dfs(edges[node], depth + 1, seen)
            visited[node] = True
            seen.pop(node)
            return res

        for node in range(n):
            if not visited[node]:
                res = dfs(node, 0, {})
                if res != -1:
                    max_cycle = max(max_cycle, res)

        return max_cycle
