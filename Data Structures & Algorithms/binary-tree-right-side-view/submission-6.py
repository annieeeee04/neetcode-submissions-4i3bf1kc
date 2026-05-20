# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque 
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        queue = deque([root])
        out = []

        while queue:
            level_size = len(queue)
            for i in range(level_size):
                cur = queue.popleft()

                if i == level_size-1:
                    out.append(cur.val)

                if cur.left: queue.append(cur.left)
                if cur.right: queue.append(cur.right)
                
        return out