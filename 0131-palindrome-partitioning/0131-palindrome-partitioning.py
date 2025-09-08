class Solution:
    def partition(self, s: str) -> List[List[str]]:


        # https://www.youtube.com/watch?v=3jvWodd7ht0
        # Trick - for loop - left to right each node
        # dfs fn - top to bottom. For left to right node, perform dfs()
        
        res = []
        part = []
        def dfs(i):
            if i >= len(s):
                res.append(part.copy())
            
            # Left to right on each node
            for j in range(i, len(s)):
                if isPalin(s, i, j):
                    part.append(s[i: j + 1])
                    # Top to bottom dfs
                    dfs(j + 1)
                    part.pop()

        
        def isPalin(s, l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
            
        dfs(0)
        return res