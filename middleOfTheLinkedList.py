# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def lengthLL(head):
            h = head
            counter = 0
            while h:
                h = h.next
                counter += 1
            return counter

        counter = 0
        lengthOfLinkedList = lengthLL(head)
        while counter < lengthOfLinkedList//2:
            head = head.next
            counter += 1
        return head