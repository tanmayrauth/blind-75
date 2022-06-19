class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # Reach till the middle of the LL
        # Reverse the next half of LL
        # Traverse from both end and keep on alternatively changing the next val
        
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
      
        # Reversing the next half LL
        prev    = None
        current = slow
        
        while current:
            nxtNode      = current.next
            current.next = prev
            
            prev    = current
            current = nxtNode
             
        # Step 3
        temp = head
        while temp and temp.next and prev.next:
            # Save next node value
            nextTemp = temp.next
            nextPrev = prev.next
            
            # Modify list structure to create as alternate edge node & then correct traversing with temp.next.next = nextTemp
            temp.next = prev 
            temp.next.next = nextTemp
            
            # Assigining temp and prev values since it will be then used in next cycle
            temp = nextTemp
            prev = nextPrev

