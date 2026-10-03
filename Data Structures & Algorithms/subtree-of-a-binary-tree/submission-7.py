# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def areSameTree(node1, node2):
            if not node1 and not node2:
                return True
            if not node1 or not node2:
                return False
            if node1.val != node2.val:
                return False
            
            left = areSameTree(node1.left, node2.left)
            right = areSameTree(node1.right, node2.right)
            return left and right

        if not root and subRoot:
            return False
        if areSameTree(root, subRoot):
            return True
        leftCheck = self.isSubtree(root.left, subRoot)
        rightCheck = self.isSubtree(root.right, subRoot)
        return leftCheck or rightCheck
