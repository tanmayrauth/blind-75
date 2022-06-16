"""
Interating through the nodes. 
4 steps with 2 base variable(prev, current) is needed to solve this prblem
Just Imagine how you will be using these 2 variables to reverse direction of 2 nodes and update the current ptr

"""

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None 
        curr = head
        
        while curr:
            nxt = curr.next 
            curr.next = prev
            
            #Getting ready for next iteration of node
            prev = curr
            curr = nxt
            
        return prev
        