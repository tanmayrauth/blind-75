"""
Intuition:
    Run one ptr at double speed of other. Now that fast ptr is running fast incase of cycle the fast ptr will point to slow ptr atleast once.
    During that scenario we will return True.
    Now in case there is no cycle the fast ptr will reach None value and our While loop will break and then we return False
"""

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = slow = head
        
        while( fast and fast.next ):
            fast = fast.next.next
            slow = slow.next
            
            if fast == slow:
                return True
            
        return False
        