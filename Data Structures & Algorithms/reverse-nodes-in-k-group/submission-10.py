# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 1 :
            return head
        
        
        def reverseLL(head):
            if not head or not head.next:
                return head
            
            newHead = reverseLL(head.next)
            head.next.next = head
            head.next = None
            return newHead


        #for each sub ll, we need the initial head, the initial tail and the tail.next pointer
        dummy = ListNode(0)
        dummy.next = head
        groupPrev = dummy
        while True:
            kth = groupPrev
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next
            groupStart = groupPrev.next
            nextGroup = kth.next

            kth.next = None

            reversedHead = reverseLL(groupStart)
            groupPrev.next = reversedHead
            groupPrev = groupStart
            groupPrev.next = nextGroup
            

        return dummy.next 

