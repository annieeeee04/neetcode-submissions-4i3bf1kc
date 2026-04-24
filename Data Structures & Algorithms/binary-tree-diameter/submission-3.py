# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Time: O(n)
# Space: O(h)
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def getHeight(node):
            if not node:
                return 0
            
            left = getHeight(node.left)
            right = getHeight(node.right)

            self.res = max(self.res, left + right)
            return 1 + max(left, right)
        getHeight(root)
        return self.res