# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ans = root.val

        def dfs(node):
            if not node: return 0

            leftMax = max(0, dfs(node.left))
            rightMax = max(0, dfs(node.right))

            self.ans = max(self.ans, node.val + leftMax + rightMax)
            return max(leftMax, rightMax) + node.val
        
        dfs(root)
        return self.ans
        