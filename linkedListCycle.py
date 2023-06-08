# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        if not head or not head.next or not head.next.next:
            return False

        slowP = head
        fastP = head.next

        while fastP != None and fastP.next != None:
            if slowP == fastP:
                return True
            slowP = slowP.next
            fastP = fastP.next.next
        
        return False