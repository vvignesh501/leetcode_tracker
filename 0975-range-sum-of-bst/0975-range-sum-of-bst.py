# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

        self.res = []
        def dfs(root, left, right):

            if not root:
                return None

            if low <= root.val <= high:
                self.res.append(root.val)

            dfs(root.left, low, high)
            dfs(root.right, low, high)
        
        dfs(root, low, high)
        return sum(self.res)