class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:

        # Creates a 3*3 matrix for n = 3 [0, 0, 0] 
        # then [[0, 0, 0] [0, 0, 0]] 
        # then [[0, 0, 0] [0, 0, 0] [0, 0, 0]]
        res = [[0]*n for _ in range(n)]

        l = 0
        r = len(res[0])
        t = 0
        b = len(res)
        inc = 1

        while l < r and t < b:

            for i in range(l, r):
                res[t][i] = inc
                inc += 1
            t += 1

            for i in range(t, b):
                res[i][r - 1] = inc
                inc += 1
            r -= 1

            if not(t < b and l < r):
                break

            for i in range(r-1, l-1, -1):
                res[b-1][i] = inc
                inc += 1
            b -= 1
            
            for i in range(b-1, t-1, -1):
                res[i][l] = inc
                inc += 1
            l += 1
        
        return res
    

# Time - O(m * n)
# Space - O(m * n)