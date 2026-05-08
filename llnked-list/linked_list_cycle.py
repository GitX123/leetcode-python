from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

'''
1. Create a slow and faster pointer.
2. Slow pointer moves one step while faster pointer moves 2 steps forward each time.
3. If slow pointer and faster pointer overlaps, then if a cycled linked list.
'''
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        isCycled = False
        slow_p, fast_p = head, head

        while fast_p and fast_p.next:
            slow_p = slow_p.next
            fast_p = fast_p.next.next
            if slow_p == fast_p:
                isCycled = True
                break

        return isCycled