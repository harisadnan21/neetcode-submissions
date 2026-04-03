# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        currPtr = head
        while currPtr:
            tmp = currPtr.next
            currPtr.next = prev
            prev = currPtr
            currPtr = tmp

        return prev

        
        