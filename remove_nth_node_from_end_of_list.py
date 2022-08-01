# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        def get_size(head):
            counter = 0
            h = head
            while h:
                counter+=1
                h=h.next
            return counter
        
        size = get_size(head)
        
        if n == 1 and size == 1:
            return ListNode("")
        
        skip_node = size-n
        if skip_node == 0:
            if size > 1:
                head = head.next
                return head
        # 1->2->3->4->5
        # 5-2 = 3
        index = 0
        h = head
        while head:
            if index == skip_node-1:
                print(head)
                head.next = head.next.next
            head = head.next
            index+=1
        print(h)
        return h
                
                