class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        #Solution 1 - Optimal  
        # When k > n we modulo to find the no of rotations needed
        # After k = n, the no of rotations are same
        n = len(nums)
        k = k % n

        def swap(l, r):
            while l <= r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        swap(0, n - 1)
        swap(0, k - 1)
        swap(k, n-1)

# Time - O(n)
# Space - O(1)

        # Solution 2 
        # k = k % len(nums)
        # if k != 0:
        #     nums[:k], nums[k:] = nums[-k:], nums[:-k]
# Time - O(n)
# Space - O(n) saves k values in memory while swapping

