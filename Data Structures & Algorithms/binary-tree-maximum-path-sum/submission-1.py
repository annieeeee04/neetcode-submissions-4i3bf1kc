# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # the global variable to be returned
        self.res = root.val

        def dfs(root):
            if not root:
                return 0
            
            left_max = dfs(root.left)
            right_max = dfs(root.right)
            left_max = max(left_max, 0)
            right_max = max(right_max, 0)

            # the returned value is the sum of left_max with right_max 
            # and the current node's value(including splitting)
            self.res = max(self.res, root.val + left_max + right_max)
            # The return value is the max sum start from this node
            # to its bottom child without splitting
            return max(left_max, right_max) + root.val
        
        dfs(root)
        return self.res