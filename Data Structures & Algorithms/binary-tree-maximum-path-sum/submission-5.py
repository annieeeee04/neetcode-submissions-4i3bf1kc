# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Time: O(n)
# Space: O(h)

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ans = root.val

        def dfs(node):
            if not node: return 0

            # drop a branch if it's negative (0 = skip it)
            leftMax = max(0, dfs(node.left))
            rightMax = max(0, dfs(node.right))

            # "V" shape peaking here — both branches, can't extend up
            self.ans = max(self.ans, node.val + leftMax + rightMax)
            # only one branch can extend to the parent
            return max(leftMax, rightMax) + node.val
        
        dfs(root)
        return self.ans
        