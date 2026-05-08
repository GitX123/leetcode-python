from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

'''
Iterative Solution
1. Use two pointers to iterate throgh the node pairs.
2. Reverse pointer direction of each node pairs.
'''
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev_p, curr_p = None, head

        while curr_p:
            temp = curr_p.next
            curr_p.next = prev_p
            prev_p = curr_p
            curr_p = temp

        return prev_p
    
'''
Recursive Solution
1. The stop condition is when we reach null.
2. The recursive operation is:
    a. Reverse remainder nodes except for the head.
    b. Point the reversed list to the head. 
    c. Point head to null.
    d. Return tail (new head).
3. reverse(n) = null <- a0 <- reverse(n-1)
'''
class Solution2:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # base case
        if not head: # 0 element
            return None
        
        if not head.next: # 1 element
            head.next = None
            return head
        
        # recursive case (more than 1 element)
        newHead = self.reverseList(head.next)
        head.next.next = head
        head.next = None

        return newHead