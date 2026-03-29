# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ''
        
        res = []
        queue = deque([root])

        while queue:
            cur = queue.popleft()
            if cur:
                res.append(str(cur.val))
                queue.append(cur.left)
                queue.append(cur.right)
            else:
                res.append('N')
        return ','.join(res) # '1, 2, 3, N, N, 4, 5'
            
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
        
        vals = data.split(',') # ['1', '2', '3', 'N', 'N', '4', '5']
        root = TreeNode(int(vals[0]))
        queue = deque()
        queue.append(root)
        i = 1

        while queue and i < len(vals):
            cur = queue.popleft()

            if vals[i] != 'N':
                cur.left = TreeNode(int(vals[i]))
                queue.append(cur.left)
            i += 1
            
            if i < len(vals) and vals[i] != 'N':
                cur.right = TreeNode(int(vals[i]))
                queue.append(cur.right)
            i += 1
        
        return root
