# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Time: O(n)
# Space: O(n)
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.preIdx = 0
        inMap = {val: i for i, val in enumerate(inorder)}

        def build(left, right):
            if left > right:
                return None
            
            rootVal = preorder[self.preIdx]
            self.preIdx += 1
            root = TreeNode(rootVal)

            mid = inMap[rootVal]
            root.left = build(left, mid - 1)
            root.right = build(mid+1, right)
            return root
        
        return build(0, len(inorder)-1)
