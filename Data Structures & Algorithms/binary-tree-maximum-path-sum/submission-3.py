# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # res records the global max which doesn't
        # need to pass the root
        self.res = root.val

        # dfs only return the max path sum that 
        # can be reached from one side
        def dfs(node):
            if not node: return 0
            # if the sub left/right path is negative, skip
            left_max = max(0, dfs(node.left))
            right_max = max(0, dfs(node.right))
            self.res = max(self.res, node.val + left_max + right_max)

            return max(left_max, right_max) + node.val
        
        dfs(root)
        return self.res