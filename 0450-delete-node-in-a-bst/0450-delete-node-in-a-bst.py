# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)   # update root.left
        elif key > root.val:
            root.right = self.deleteNode(root.right, key) # update root.right
        else:
            # Case 1: No left child
            if not root.left:
                return root.right
            # Case 2: No right child
            if not root.right:
                return root.left

            # Case 3: Two children → find inorder successor
            succ = root.right
            while succ.left:
                succ = succ.left

            root.val = succ.val  # Replace with successor's value
            root.right = self.deleteNode(root.right, succ.val)  # Delete successor

        return root

# Aspect	Complexity
# Time	O(h), h = tree height (O(log n) for balanced BST, O(n) worst case skewed)
# Space	O(h) recursion stack

        