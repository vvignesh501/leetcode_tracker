# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        res = []
        all_nodes = ""
        def treePaths(root, all_nodes):
            if not root:
                return 
            
            # Build path string
            if all_nodes:
                all_nodes += "->" + str(root.val)
            else:
                all_nodes = str(root.val)

            if not root.left and not root.right:
                res.append(all_nodes)
                all_nodes = ""

            treePaths(root.left, all_nodes)
            treePaths(root.right, all_nodes)

        treePaths(root, all_nodes)
        return res
        
# Time: O(n) — visit every node once, each leaf path string costs O(h)

# Space: O(h) recursion stack + O(n·h) for storing paths