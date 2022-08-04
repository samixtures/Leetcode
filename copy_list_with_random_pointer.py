class ListNode:
    def __init__(self, x, next=None, random=None):
        self.val = x
        self.next = next
        self.random = random
def print_node(n):
    h = n
    while h:
        print(h.val)
        h = h.next

head = ListNode(7, ListNode(13, ListNode(11, ListNode(10, ListNode(1, None, 0), 2), 4), 0), None)

new_node = ListNode(head.val)
ret = new_node
new_node.random = head.random
head = head.next
while head:
    temp = ListNode(head.val)
    temp.random = head.random
    new_node.next = temp
    new_node = new_node.next
    head = head.next
    

# print(new_node)
# return new_node