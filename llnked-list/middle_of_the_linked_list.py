from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

'''
1. Create a fast and slow pointers.
2. Slow pointer moves 1 step and fast pointer moves 2 steps at a time.
3. The two pointers stop moving once the fast pointer or its next pointer points to null.
'''
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow_p, fast_p = head, head

        while fast_p and fast_p.next:
            fast_p = fast_p.next.next
            slow_p = slow_p.next
        
        return slow_p