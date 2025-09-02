# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        self.balance = True
        def height(root):
            # Initially the balance is True and height is 0
            if not root:
                return 0    

            leftNode = height(root.left)
            rightNode = height(root.right)

            diff = abs(leftNode - rightNode) 
            print(root.val, leftNode, rightNode)
            
            if diff > 1:
                self.balance = False
                return self.balance
            
            return 1 + max(leftNode, rightNode)
           
        
        height(root)
        return False if self.balance == False else True