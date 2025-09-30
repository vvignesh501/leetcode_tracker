# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:

        self.min_diff = float("inf")
        self.prev = None
        def minDiff(root):
            if not root:
                return 0
            
            minDiff(root.left)

            if self.prev is not None:
                self.min_diff = min(self.min_diff, root.val - self.prev)
            self.prev = root.val

            minDiff(root.right)
        
        minDiff(root)
        return self.min_diff