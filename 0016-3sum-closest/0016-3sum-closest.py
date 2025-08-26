class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        result = nums[0] + nums[1] + nums[2]
        
        if len(nums) == 3:
            return sum(nums)

        for i in range(len(nums) -2):
            
            # update: ignore the duplicate numbers to fast the result
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            j, k = i+1, len(nums)-1
            while j < k:
                curSum = nums[i] + nums[j] + nums[k]
                if curSum == target: 
                    return curSum
                elif curSum > target: 
                    k -= 1
                else: 
                    j += 1
                if abs(target-curSum) < abs(result-target):
                    result = curSum
        return result
                
                
# Time = O(n**2)
# Space = O(1)