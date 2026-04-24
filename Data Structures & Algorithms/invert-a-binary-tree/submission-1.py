# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Time: O(n)
# Space: O(h) , in recursion we have use callStack
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: 
            return root
        
        left = self.invertTree(root.right)
        right = self.invertTree(root.left)

        root.left = left
        root.right = right

        return root