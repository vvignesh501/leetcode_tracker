class Solution:
    def countArrangement(self, n: int) -> int:
        
        res = set()
        def backtracking(pos, res):

            if pos > n:
                return 1
            
            count = 0
            for i in range(1, n + 1):
                if i not in res and (i % pos == 0 or pos % i == 0):
                    res.add(i)
                    count += backtracking(pos + 1, res)
                    res.remove(i)
            return count
        
        return backtracking(1, res)

# Time - O(n!)
# Space - O(n)