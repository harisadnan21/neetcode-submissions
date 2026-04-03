"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # copy first list with next only 
        # create hashmap original nodes to copies
        # progress ptr in copy and original list
        ptr = head 
        newptr = Node(ptr.val) if ptr else None
        headsecond = newptr
        corr = dict()
        corr[ptr] = newptr
        while ptr:
            ptr = ptr.next
            newptr.next = Node(ptr.val) if ptr else None
            newptr = newptr.next
            corr[ptr] = newptr

        ptr = head
        newptr = headsecond
        while ptr:
            rdmsecond = corr[ptr.random]
            newptr.random = rdmsecond
            ptr = ptr.next
            newptr = newptr.next
        return headsecond

            
            
