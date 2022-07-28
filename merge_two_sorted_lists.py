# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # 1->2->4->Null
        # 1->3->4->Null
        # 1->2->3->4->Null
        
        # 1->3->5->Null
        # 2->4->6->Null
        # 1->2->3->4->5->6->Null
        
        if not list1:
            return list2
        elif not list2:
            return list1
        
        if list1.val <= list2.val:
            ret = ListNode(list1.val)
            list1 = list1.next
        else:
            ret = ListNode(list2.val)
            list2 = list2.next
        
        final = ret
        
        while list1 and list2:
            if list1.val <= list2.val:
                ret.next = ListNode(list1.val)
                ret = ret.next
                list1 = list1.next
            elif list1.val >= list2.val:
                ret.next = ListNode(list2.val)
                ret = ret.next
                list2 = list2.next
        
        if list1:
            while list1:
                ret.next = ListNode(list1.val)
                ret = ret.next
                list1 = list1.next
        if list2:
            while list2:
                ret.next = ListNode(list2.val)
                ret = ret.next
                list2 = list2.next
        return final