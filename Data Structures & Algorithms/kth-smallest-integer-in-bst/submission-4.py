# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Time: O(n log k) , heappush -> log k, do it for n times
# Space: O(n + k) , n for stack, k for maxHeap
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = [root]
        maxHeap = []
        while stack:
            cur = stack.pop()
            heapq.heappush(maxHeap, -cur.val)
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)
            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)
        
        return -maxHeap[0]