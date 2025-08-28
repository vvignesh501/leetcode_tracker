class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        output = []
        res = []
        
        def backtracking(openN, closeN):
            if openN == closeN == n:
                output.append("".join(res))
                return
            
            if openN < n:
                res.append("(")
                backtracking(openN + 1, closeN)
                res.pop()
            
            if closeN < openN:
                res.append(")")
                backtracking(openN, closeN + 1)
                res.pop()
            return output
            
        backtracking(0, 0)
        return output

# Time = O(2^2*n)) instead 2^n - there are 2 choices for every 2n possibilities
# Space = O(n)