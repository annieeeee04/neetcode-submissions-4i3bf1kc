# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        queue = deque()
        queue.append(root)
        while queue:
            size = len(queue)
            while size > 1:
                cur = queue.popleft()
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
                size -= 1
            see = queue.popleft()
            if see.left:
                    queue.append(see.left)
            if see.right:
                    queue.append(see.right)
            res.append(see.val)
        
        return res