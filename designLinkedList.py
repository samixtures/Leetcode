class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        """
        3->5->2->7->None
        0  1  2  3

        index = 2, return 5

        we should create a counter variable starting at 0
        while head:
            if counter == index:
                return head.val
            counter += 1
            head = head.next
        """
        counter = 0
        h = self.head
        while h:
            if counter == index:
                return h.val
            counter += 1
            h = h.next

    def addAtHead(self, val: int) -> None:
        temp = self.head
        self.head = Node(val, temp)

    def addAtTail(self, val: int) -> None:
        """
        3->5->2->7->None
        0  1  2  3

        Need to get to 7, set 7's next to the new node, set new node's next to None
        We get to 7 by doing while head.next
        """
        h = self.head
        if h:
            while h.next:
                h = h.next
            newNode = Node(val, None)
            h.next = newNode


    def addAtIndex(self, index: int, val: int) -> None:
        """
        3->5->2->7->None
        0  1  2  3

        given an index and a val add a new node with value val to that specific index
        addAtIndex(1, 9)
        3->9->5->2->7->None
        0  1  2  3  4

        Create counter variable to keep track of what index we are at.
        Traverse until we get to the index before the index we want to add the new node to.
        So if index == 1, then traverse until counter == 0.

        Once we are on 0, save its next in a temp, then change its next to be newNode(val, temp)


        There will be edge cases with the way I'm going to write code. I think the big one is if index == 0.


        """

        # edge case index == 0
        if index == 0:
            self.addAtHead(val)

        h = self.head
        counter = 0
        while h:
            if counter == index-1:
                temp = h.next
                newNode = Node(val, temp)
                h.next = newNode
                # return
            counter += 1
            h = h.next

    def deleteAtIndex(self, index: int) -> None:

        # edge case: if index == 0
        if index == 0:
            if self.head.next:
                self.head = self.head.next

        counter = 0
        h = self.head
        while h:
            if counter == index-1:
                temp = h.next.next
                h.next = temp
                # return
            counter += 1
            h = h.next

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)