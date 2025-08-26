class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # To remove the duplicates, sort the nums
        nums.sort()
        result = []
        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1

            if i > 0 and nums[i] == nums[i-1]:
                continue  # skip duplicate i

            while j < k:
                threeSum = nums[i] + nums[j] + nums[k]
                if threeSum == 0:
                    result.append([nums[i], nums[j], nums[k]])

                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1

                    j += 1
                    k -= 1

                elif threeSum < 0:
                    j += 1
                else:
                    k -= 1
            
        return result
