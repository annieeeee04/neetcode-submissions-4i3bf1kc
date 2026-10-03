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
        
        res = 0
        stack = [(root, root.val)]
        while stack:
            cur, max_sofar = stack.pop()
            if cur.val >= max_sofar:
                res += 1
                max_sofar = cur.val
            if cur.left: stack.append((cur.left, max_sofar))
            if cur.right: stack.append((cur.right, max_sofar))
        return res