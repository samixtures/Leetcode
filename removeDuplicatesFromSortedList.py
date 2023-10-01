# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        deleting duplicates of a linked list and returning the head of the 
        linked list without duplicates

        when we arrive at a node with a number we haven't seen before then 
        we add it to our set
        otherwise we set the previous node equal to previous.next.next

        Time Complexity: O(n), we iterate through each node once, and use   conditionals to change their "next" pointers

        Space Complexity: O(n) worst case if there are only unique values, then
        the set will contain all of the values
        """
        res = head
        h = head
        prev = head
        duplSet = set()
        while h:
            if h.val not in duplSet:
                duplSet.add(h.val)
                prev = h
            else:
                prev.next = prev.next.next
            h = h.next 
        return res