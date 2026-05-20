# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        num = 0
        stack = [(root, float('-inf'))]

        while stack:
            cur, max_so_far  = stack.pop()
            if cur.val >= max_so_far :
                num += 1
            new_max= max(max_so_far, cur.val)
            
            if cur.left:
                stack.append((cur.left, new_max))
            if cur.right:
                stack.append((cur.right, new_max))

        return num
