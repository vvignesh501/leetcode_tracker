class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        n = len(isConnected)
        count = 0
        visited = set()

        def dfs(i):
            # This is enumerate. Node - index, edges = [1,1,0]
            for node, edges in enumerate(isConnected[i]):

                # Perform dfs only if the value == 1 and not visited.
                if edges == 1 and node not in visited:
                    visited.add(node)
                    dfs(node)


        for i in range(n):
            if i not in visited:
                count += 1
                dfs(i)
        
        return count