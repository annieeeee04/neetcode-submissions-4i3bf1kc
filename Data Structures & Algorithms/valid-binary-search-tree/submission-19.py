# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        stack = [(root, float('-inf'), float('inf'))]

        while stack:    
            cur, min_sofar, max_sofar = stack.pop()
            if cur.val <= min_sofar or cur.val >= max_sofar:
                return False
            
            if cur.left:
                stack.append((cur.left, min_sofar, cur.val))
            if cur.right:
                stack.append((cur.right, cur.val, max_sofar))

        return True