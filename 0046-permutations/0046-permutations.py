class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        perms=[]
        solution=[]

        def backtrack():
            if len(solution)==len(nums):
                perms.append(solution.copy())
                return 

            for num in nums:
                if num not in solution:
                    solution.append(num)
                    backtrack()
                    solution.pop()
                    
        backtrack()
        return perms

# Metric	Complexity
# Time	O(n!) — all permutations
# Space	O(n) recursion stack