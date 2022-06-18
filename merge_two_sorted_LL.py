"""
First comapare this question with merge k sorted linked list.
Intuition is that since both the LL is sorted we jst need to just compare nodes from each List and arrange them appropriately.

First if we create a dummy node which will work as current ptr then using while loop we can set its next element by
Comparing the 2 linked list and picking the smallest node from it.
4 coniditons are used to select the smallest next node.

"""

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        head = ListNode( 0, None )
        p    = head
        
        while True:
            if not list1:
                p.next = list2
                break
                
            if not list2:
                p.next = list1
                break
                  
            if list1.val < list2.val:
                p.next = list1
                list1  = list1.next
            else:
                p.next = list2
                list2  = list2.next
                
            p = p.next
            
        return head.next