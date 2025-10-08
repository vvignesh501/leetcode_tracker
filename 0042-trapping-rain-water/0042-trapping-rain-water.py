class Solution:
    def trap(self, height: List[int]) -> int:

        left = 0
        right = len(height) -1
        max_left = 0
        max_right = 0
        water = 0

        while left <= right:
            if height[left] <= height[right]:

                # if curret index > prev left, make current index as max left
                if height[left] >= max_left:
                    max_left = height[left]
                else:
                    water += max_left - height[left]
                left += 1
            else:
                # if curret index > prev right, make current index as max left
                if height[right] >= max_right:
                    max_right = height[right]
                else:
                    water += max_right - height[right]
                right -= 1
        
        return water
             

# Time Complexity: O(n)
# Space Complexity: O(1)

        