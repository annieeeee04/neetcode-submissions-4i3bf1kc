# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def inorder(node, low, high):
            if not node:
                return True
            
            if not (node.val > low and node.val < high):
                return False
            
            return (inorder(node.left, low, node.val) and 
                    inorder(node.right, node.val, high))
        
        return inorder(root, float('-inf'), float('inf'))
