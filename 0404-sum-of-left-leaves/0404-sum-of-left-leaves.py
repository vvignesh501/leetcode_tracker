# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        stack = [root]
        total = 0

        while stack:
            root = stack.pop()

            if root.left:
                if not root.left.left and not root.left.right:
                    total += root.left.val
                else:
                    stack.append(root.left)
            if root.right:
                stack.append(root.right)
        
        return total
        
# Time - O(n)
# Space - O(h)