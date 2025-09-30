# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        total = 0
        def pathSum(root, total):
            if not root:
                return False

            total += root.val
            if not root.left and not root.right:
                if total == targetSum:
                    return True

            left = pathSum(root.left, total)
            right = pathSum(root.right, total)

            return left or right
        
        return pathSum(root, 0)

# Time - O(n)
# Space - O(h)
        