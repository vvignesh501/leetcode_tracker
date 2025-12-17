# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        # Edge case: empty subtree is always a subtree
        if not subRoot:
            return True
        
        # If main tree is empty but subtree is not
        if not root:
            return False
        
        # If trees match at this node
        if self.isSameTree(root, subRoot):
            return True
        
        # Check each root.left with subRoot or root.right with subRoot
        return (
            self.isSubtree(root.left, subRoot) or
            self.isSubtree(root.right, subRoot)
        )

    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # Both nodes are null
        if not p and not q:
            return True
        
        # One is null or values differ
        if not p or not q or p.val != q.val:
            return False
        
        # Check left and right subtrees
        return (
            self.isSameTree(p.left, q.left) and
            self.isSameTree(p.right, q.right)
        )