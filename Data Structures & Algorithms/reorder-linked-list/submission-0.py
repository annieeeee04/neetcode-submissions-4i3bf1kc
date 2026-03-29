# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        part2 = slow.next
        slow.next = None

        prev = None
        head2 = part2
        while head2:
            nxt = head2.next
            head2.next = prev
            prev = head2
            head2 = nxt
        part2 = prev

        while part2:
            temp1, temp2 = head.next, part2.next
            head.next = part2
            part2.next = temp1
            head = temp1
            part2 = temp2
