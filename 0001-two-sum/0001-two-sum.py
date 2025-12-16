class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        d = {}
        
        for i, n in enumerate(nums):
            diff = target - n
            if n in d:
                return [d[n], i]
            else:
                d[diff] = i
            


# Time complexity = O(n)
# Space complexity = O(n)


        