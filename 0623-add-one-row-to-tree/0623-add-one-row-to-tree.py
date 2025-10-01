# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        
        # Special case: if depth = 1, create new root
        if depth == 1:
            new_root = TreeNode(val)
            new_root.left = root
            return new_root
        
        def dfs(node, curr_depth):
            if not node:
                return
            
            # When we reach depth - 1, we insert the new row
            if curr_depth == depth - 1:
                old_left = node.left
                old_right = node.right

                node.left = TreeNode(val)
                node.left.left = old_left

                node.right = TreeNode(val)
                node.right.right = old_right
                return  # Done inserting at this level
            
            # Recurse further
            dfs(node.left, curr_depth + 1)
            dfs(node.right, curr_depth + 1)
        
        dfs(root, 1)
        return root

# Time = O(n)
# Space = O(h)