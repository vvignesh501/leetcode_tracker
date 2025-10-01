# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        
        self.count = 0
        def countNode(root):
            if not root:
                return 0

            self.count += 1
            countNode(root.left)
            countNode(root.right)
        
        countNode(root)
        return self.count