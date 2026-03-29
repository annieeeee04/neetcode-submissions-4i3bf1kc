# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        heap = []
        stack = []
        stack.append(root)
        while stack:
            cur = stack.pop()
            heapq.heappush(heap, -cur.val)
            while len(heap) > k:
                heapq.heappop(heap)
            if cur.left: stack.append(cur.left)
            if cur.right: stack.append(cur.right)

        return - heap[0]