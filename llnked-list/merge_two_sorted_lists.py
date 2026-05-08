from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

'''
1. Create a head node for our solution
2. Compare each node iteratively in the two lists, and attach the smaller one 
3. Attach the rest nodes
'''
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        tail = head

        # step 2
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        # step 3
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        return head.next