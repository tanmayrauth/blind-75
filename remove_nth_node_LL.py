"""
Intuition is that we need kth node from right. So what if we have slow and fast ptr and build this logic.
Your fast ptr should run for n times first. This way you will be 1 position ahead of n.
Since you're 1 position ahead of n your while loop must be on fast.next and not on fast.
Because your slow ptr must point to n-1th location from right and not nth location from right. So that you can do slow.next = slow.next.next
"""

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        fast = slow = head
        
        for i in range(n):   
            fast = fast.next
            
        if not fast:        #Case for handling the edge case of [1] and 1
            return head.next
        
        while fast.next:
            fast = fast.next
            slow = slow.next 
            
        slow.next = slow.next.next 
        return head