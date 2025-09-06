# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root, left_min_val, right_max_val):

            if not root:
                return True
            
            # <- wrong: this returns False when node IS not valid
            # otherwis continue with the children
            if not (left_min_val < root.val < right_max_val):
                return False

            return (dfs(root.left, left_min_val, root.val) and dfs(root.right, root.val, right_max_val))
 
        
        return dfs(root, float("-inf"), float("inf"))

        