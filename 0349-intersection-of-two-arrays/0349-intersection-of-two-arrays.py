class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        return list(set(nums1) & set(nums2))

# Time - O(n + m)
# Space - O(n + m)