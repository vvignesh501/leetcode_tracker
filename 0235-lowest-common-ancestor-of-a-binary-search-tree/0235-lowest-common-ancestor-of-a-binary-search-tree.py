# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        if not root:
            return None  # base case: empty tree
        
        # If root is one of p or q, return it
        if root == p or root == q:
            return root
        
        # Recurse left and right
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        # If p and q are found in different subtrees → root is LCA
        if left and right:
            return root
        
        # Otherwise, return the non-None child
        return left or right
