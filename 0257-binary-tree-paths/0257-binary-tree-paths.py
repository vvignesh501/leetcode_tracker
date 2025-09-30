# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        res = []
        path = ""
        def treePaths(root, path):
            if not root:
                return 
            
            # Build path string
            if path:
                path += "->" + str(root.val)
            else:
                path = str(root.val)

            if not root.left and not root.right:
                res.append(path)
                path = ""

            treePaths(root.left, path)
            treePaths(root.right, path)

        treePaths(root, path)
        return res
        
# Time: O(n) — visit every node once, each leaf path string costs O(h)

# Space: O(h) recursion stack + O(n·h) for storing paths