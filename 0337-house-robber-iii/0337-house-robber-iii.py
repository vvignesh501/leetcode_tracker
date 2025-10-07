# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root):
        from functools import lru_cache

        @lru_cache(None)
        def dfs(node):
            if not node:
                return 0

            # Rob this node
            rob_this = node.val
            if node.left:
                rob_this += dfs(node.left.left) + dfs(node.left.right)
            if node.right:
                rob_this += dfs(node.right.left) + dfs(node.right.right)

            # Skip this node
            skip_this = dfs(node.left) + dfs(node.right)

            return max(rob_this, skip_this)

        return dfs(root)
