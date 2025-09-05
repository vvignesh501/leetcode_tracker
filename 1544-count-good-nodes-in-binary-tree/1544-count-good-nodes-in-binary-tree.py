# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, max_so_far):
            if not node:
                return 0

            # node is good if its value >= max seen so far
            good = 1 if node.val >= max_so_far else 0

            # update max_so_far
            max_so_far = max(max_so_far, node.val)

            # explore children
            good += dfs(node.left, max_so_far)
            good += dfs(node.right, max_so_far)

            return good

        return dfs(root, root.val)



# Time: O(n) → every node is visited once.

# Space:

# O(h) for DFS recursion (h = tree height).

# O(w) for BFS queue (w = max width of tree).