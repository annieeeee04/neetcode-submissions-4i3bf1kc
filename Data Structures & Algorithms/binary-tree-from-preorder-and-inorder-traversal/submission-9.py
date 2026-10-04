# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Time: O(n), each node processed once, O(1) hashmap lookups
# Space: O(n), for the hashmap (plus O(h) recursion stack)

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inMap = {val: i for i, val in enumerate(inorder)}
        self.preIdx = 0

        # left/right = index bounds into inorder for this subtree
        def build(left, right):
            if left > right:
                return None

            # preorder is read sequentially — next value is always
            # the next root, no slicing/bounds needed
            rootVal = preorder[self.preIdx]
            self.preIdx += 1
            root = TreeNode(rootVal)

            # mid splits inorder into left subtree / right subtree
            mid = inMap[rootVal]
            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)
            return root

        return build(0, len(inorder) - 1)