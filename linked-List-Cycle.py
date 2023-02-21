# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if  self.hasCycle(head):
           
        
            fast,slow ,ptr = head,head,head
            while fast :
                fast = fast.next.next
                slow=slow.next
                if slow == fast:
                    break
            while slow !=ptr:
                slow = slow.next
                ptr = ptr.next
            return ptr
            
            
            
    def hasCycle(self, head):
        fast,slow= head,head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
            if fast == slow :
                return True
        return False 
