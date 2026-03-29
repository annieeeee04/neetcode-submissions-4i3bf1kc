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

        num = 0
        # path-dependent problem : must carry path state(max_so_far)
        stack = [(root, root.val)]
        while stack:
            cur, max_so_far = stack.pop()

            if cur.val >= max_so_far:
                num += 1
            
            max_so_far = max(cur.val, max_so_far)

            if cur.right:
                stack.append((cur.right, max_so_far))
            if cur.left:
                stack.append((cur.left, max_so_far))
        
        return num