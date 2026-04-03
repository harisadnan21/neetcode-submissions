# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def mergeTwoLists(list1, list2):
            head = curr = ListNode()
            if not list1:
                return list2
            if not list2:
                return list1

            while list1 and list2:
                if list1.val <= list2.val:
                    curr.next = list1
                    list1 = list1.next


                else:
                    curr.next = list2
                    list2 = list2.next
                
                curr = curr.next    
            #handle the case in which the lists do not have the same lengths
            if list1:
                curr.next = list1
            else:
                curr.next = list2
            
            return head.next

        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]
        
        while len(lists) > 1:
            print(lists)
            mergedlist = []
            for i in range(0, len(lists), 2):
                if i == len(lists) - 1:
                    mergedlist.append(mergeTwoLists(lists[i], None))
                else:
                    mergedlist.append(mergeTwoLists(lists[i], lists[i + 1]))
            lists = mergedlist
                
        return lists[0]




















        # def mergeTwoLists(list1, list2):
        #     A = list1
        #     B = list2
        #     if not A:
        #         return B
        #     if not B:
        #         return A
        #     head = None
        #     prevA = None
        #     prevB = None
        #     #handle first element
        #     if A.val <= B.val:
        #         head = A
        #         prevA = A
        #         A = A.next
        #     else:
        #         head = B
        #         prevB = B
        #         B = B.next   
        #     while A or B:
        #         print(A.val, B.val)
        #         if A.val <= B.val:
        #             prevB.next = A
        #             prevA = A
        #             A = A.next
        #         else:
        #             prevA.next = B
        #             prevB = B
        #             B = B.next
        #         if not A:
        #             print(A.val if A else None, prevA.val if prevA else None)
        #             prevA.next = B
        #             return head
        #         if not B:
        #             prevB.next = A
        #             return head
        #     return head

        # for i in range(1, len(lists)):

        #     head = mergeTwoLists(lists[i], lists[i -1])
        #     lists[i] = head
        # return lists[len(lists) -1]
