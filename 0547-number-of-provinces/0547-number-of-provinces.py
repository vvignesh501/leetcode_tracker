class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = set()

        def dfs(city):
            for nei in range(n):
                if isConnected[city][nei] == 1 and nei not in visited:
                    visited.add(nei)
                    dfs(nei)

        provinces = 0
        for i in range(n):
            if i not in visited:
                provinces += 1
                visited.add(i)
                dfs(i)
        
        return provinces
