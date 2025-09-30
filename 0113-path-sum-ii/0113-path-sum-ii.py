# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

        self.trackNodes = []
        res = []
        def pathSumTwo(root, total, trackNodes):
            if not root:
                return None

            total += root.val
            self.trackNodes.append(root.val)

            # leaf node check
            if not root.left and not root.right:
                if total == targetSum:
                    res.append(self.trackNodes.copy())

            pathSumTwo(root.left, total, self.trackNodes)
            pathSumTwo(root.right, total, self.trackNodes)

            self.trackNodes.pop()

            return self.trackNodes
        
        pathSumTwo(root, 0, self.trackNodes)
        return res

# Time: O(n·h), worst O(n²), average O(n log n)

# Space: O(n·h), due to result storage + recursion