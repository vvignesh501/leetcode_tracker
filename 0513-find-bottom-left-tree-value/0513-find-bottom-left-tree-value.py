# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        
        self.max_depth = 0
        self.leftmost_val = root.val
        def getBottomValue(root, depth):

            if not root:
                return

            if depth > self.max_depth:
                self.max_depth = depth
                self.leftmost_val = root.val
            
            getBottomValue(root.left, depth + 1)
            getBottomValue(root.right, depth + 1)
        
        getBottomValue(root, 1)
        return self.leftmost_val


# Time - O(n)
# Space - O(h)