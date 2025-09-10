class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        pacific, atlantic = set(), set()
        rows, cols = len(heights), len(heights[0])
        result = []

        def dfs(r, c, prevHeight, visited):
            if r < 0 or r >= rows or c < 0 or c >= cols or (r, c) in visited or heights[r][c] < prevHeight:
                return 
            
            visited.add((r, c))
            dfs(r + 1, c, heights[r][c], visited)
            dfs(r - 1, c, heights[r][c], visited)
            dfs(r, c + 1, heights[r][c], visited)
            dfs(r, c - 1, heights[r][c], visited)

        for r in range(rows):
            dfs(r, 0, 0, pacific)
            dfs(r, cols - 1, 0, atlantic)

        for c in range(cols):
            dfs(0, c, 0, pacific)
            dfs(rows-1, c, 0, atlantic)
        
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pacific and (r, c) in atlantic:
                    result.append((r, c))
        
        return result

# Time = O(m.n)
# Space = O(m.n)

        