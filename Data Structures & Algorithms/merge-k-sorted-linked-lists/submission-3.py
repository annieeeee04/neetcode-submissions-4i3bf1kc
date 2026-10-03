# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def mergeTwoLists(list1, list2):
            dummy = ListNode(0)
            cur = dummy

            while list1 and list2:
                val1, val2 = list1.val, list2.val
                if val1 <= val2:
                    cur.next = list1
                    list1 = list1.next
                else:
                    cur.next = list2
                    list2 = list2.next
                cur = cur.next
            if list1: cur.next = list1
            if list2: cur.next = list2
            return dummy.next
            
        if len(lists) == 0 or not lists:
            return None
        
        while len(lists) > 1:
            path = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if i+1 < len(lists) else None
                path.append(mergeTwoLists(l1,l2))
            lists = path
        return lists[0]

