class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.root = None
        self.top = None

    def InsertNode(self, val):
        n = Node(val)
        if self.root is None:
            self.root = n
            self.top= n
            return
        
        self.top.next = n
        n.prev = self.top
        self.top = n

    def DisplayBackward(self):
        temp = self.top
        while temp is not None:
            print(temp.val, end="<->")
            temp = temp.prev
        print("None")

dll = DoublyLinkedList()
dll.InsertNode(10)
dll.InsertNode(20)
dll.InsertNode(30)
dll.InsertNode(40)
dll.DisplayBackward()
       
