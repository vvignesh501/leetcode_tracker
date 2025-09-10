class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        courseMap = defaultdict(list)
        for node, edge in prerequisites:
            courseMap[node].append(edge)
        
        visited = set()
        def dfs(node):

            # edgeCase 1
            if courseMap[node] == []:
                return True

            # edgeCase 2
            if node in visited:
                return False
            
            visited.add(node)
            for edges in courseMap[node]:
                if not dfs(edges):
                    return False

            visited.remove(node)
            # This makes the node as done which means no cycle detected.
            # When another path, another DFS is done, this node is clean slate 
            # saying DFS through this node is non cyclic
            courseMap[node] = []
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        return True
            

# Time = O(V + E)
# Space = O(V + E)        