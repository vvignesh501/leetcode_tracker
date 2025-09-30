# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:

        self.longest = 0
        def longestPathLength(root):
            if not root:
                return 0

            left_len = longestPathLength(root.left)
            right_len = longestPathLength(root.right)
            
            left_path = right_path = 0
            if root.left and root.val == root.left.val:
                left_path = left_len + 1
            
            if root.right and root.val == root.right.val:
                right_path = right_len + 1

            self.longest = max(self.longest, left_path + right_path)
            # It's a path, we cannot return both left and right.
            # We can only choose left or the right path. max(left or right) 
            # when climbing up to top of the tree
            return max(left_path, right_path)

        longestPathLength(root)
        return self.longest

# Time - O(n)
# Space - O(h)