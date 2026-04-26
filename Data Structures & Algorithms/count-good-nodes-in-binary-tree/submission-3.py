# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        stack = [[root, root.val]]
        num = 0
        while stack:
            cur, maxSoFar = stack.pop()
            if cur.val >= maxSoFar:
                num += 1
                maxSoFar = cur.val
            
            if cur.left:
                stack.append([cur.left, maxSoFar])
            if cur.right:
                stack.append([cur.right, maxSoFar])
        return num
        