from collections import deque
class MyCircularQueue:

    def __init__(self, k: int):
        self.q = [None]*k
        # print("initialization:", self.q)
        self.head = None
        self.tail = None
        self.maxSize = k # k = 3 -> indices 0, 1, 2

    def enQueue(self, value: int) -> bool:
        if self.isFull(): return False
        
        if self.head == None: self.head = 0
        if self.tail == None: self.tail = 0
        elif self.tail == self.maxSize - 1: self.tail = 0
        else: self.tail += 1
        self.q[self.tail] = value
        # print("enQueue q is", self.q)
        return True

    def deQueue(self) -> bool:
        if self.isEmpty(): return False
        
        self.q[self.head] = None
        if self.head == self.maxSize - 1: self.head = 0
        else: self.head += 1
        # print("dequeue q is", self.q)
        return True

    def Front(self) -> int:
        if self.head != None and self.head < len(self.q):
            if self.q[self.head] != None:
                return self.q[self.head]
        if self.tail != None and self.tail < len(self.q):
            if self.q[self.tail] != None:
                return self.q[self.tail]
        return -1

    def Rear(self) -> int:
        if self.tail != None and self.tail < len(self.q):
            if self.q[self.tail] != None:
                return self.q[self.tail]
        if self.head and self.head < len(self.q):
            if self.q[self.head] != None:
                return self.q[self.head]
        return -1

    def isEmpty(self) -> bool:
        if self.head == None and self.tail == None:
            return True
        if self.q[self.head] == None and self.q[self.tail] == None:
            return True
        return False

    def isFull(self) -> bool:
        """
        if tail = head - 1
        or if tail is at the end and head is at the start?
        
        """
        if self.head != None and self.tail != None:
            if self.q[self.head] != None and self.q[self.tail] != None:
                if self.tail == self.head - 1:
                    return True
                if self.head == 0 and self.tail == self.maxSize - 1:
                    return True
        return False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()