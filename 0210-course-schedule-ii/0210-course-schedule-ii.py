class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        courseMap = defaultdict(list)
        for edge, node in prerequisites:
            courseMap[node].append(edge)
        
        visiting = set()  # tracks nodes in current path for cycle detection
        visited = set()   # tracks nodes already added to output
        output = []

        def dfs(node):
            if node in visiting:  # cycle detected
                return False
            if node in visited:   # already processed
                return True

            visiting.add(node)
            for nei in courseMap[node]:
                if not dfs(nei):
                    return False
            visiting.remove(node)

            visited.add(node)
            output.append(node)
            return True

        for course in range(numCourses):
            if not dfs(course):
                return []  # cycle detected, impossible to finish all courses
        
        return output[::-1]  # reverse for correct topological order


# Time = O(V + E)
# Space = O(V + E)