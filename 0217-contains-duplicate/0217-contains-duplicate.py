class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        hashSet = set()
        for i in nums:
            if i not in hashSet:
                hashSet.add(i)
            else:
                return True
        return False

         