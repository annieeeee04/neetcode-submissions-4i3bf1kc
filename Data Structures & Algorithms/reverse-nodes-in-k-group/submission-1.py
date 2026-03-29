# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def getKth(node, k):
            while node and k > 0:
                node = node.next
                k -= 1
            return node
        
        dummy = ListNode(0, head)
        node = dummy

        while True:
            kth = getKth(node, k)
            if not kth:
                break
                
            nextStart = kth.next
            prev = kth.next
            curr = node.next
            while curr != nextStart:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            
            temp = node.next
            node.next = prev
            node = temp
        
        return dummy.next
