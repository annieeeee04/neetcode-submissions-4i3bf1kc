# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Step 1: check if there are k nodes left
        node = head
        for _ in range(k):
            if not node:
                return head
            node = node.next
        
        # Step 2: reverse the list
        prev = None
        cur = head
        for _ in range(k):
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        
        # Step 3: recursion
        head.next = self.reverseKGroup(cur, k)

        return prev