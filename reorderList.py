# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next or not head.next.next:
            return

        slowP = head
        fastP = head.next

        while fastP and fastP.next:
            slowP = slowP.next
            fastP = fastP.next.next
            print(slowP.val)

        listMiddle = slowP

        reverseEnd = slowP.next

        prev = None
        while reverseEnd:
            nextNode = reverseEnd.next
            reverseEnd.next = prev
            prev = reverseEnd
            reverseEnd = nextNode
        reverseEnd = prev

        headRef = head
        while headRef != listMiddle and reverseEnd:
            headNext = headRef.next
            reverseNext = reverseEnd.next
            headRef.next = reverseEnd
            reverseEnd.next = headNext
            reverseEnd = reverseNext
            headRef = headNext
        if headRef.next.next:
            headRef.next = None