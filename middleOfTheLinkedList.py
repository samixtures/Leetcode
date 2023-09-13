# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 0
        nodeList = []

        while head:
            nodeList.append(head)
            head = head.next
            length += 1
        return nodeList[length//2]