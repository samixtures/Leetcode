class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        

head = ListNode(1, ListNode(2, ListNode(3)))
# 1 -> 2 -> 3 -> None
# 2 -> 1 -> None
# while saving 3 somewhere

# head1 = ListNode(1, ListNode(2)) 
# 1 -> 2 -> None
# 2 -> 1 -> None

temp = head
temp1 = temp.next # Swap this and temp2
temp2 = None # Swap this and temp1



temp1 = temp.next
temp.next = temp2
temp2 = temp
temp = temp1

temp1 = temp.next
temp.next = temp2
temp2 = temp
temp = temp1

temp1 = temp.next
temp.next = temp2
temp2 = temp
temp = temp1


while temp2:
    print(temp2.val)
    temp2 = temp2.next
