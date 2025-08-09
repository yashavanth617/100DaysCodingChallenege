class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class SingleLinkedList:
    def __init__(self):
        self.root = None

    def InsertNode(self, val, pos):
        n = Node(val)
        if self.root is None:
            self.root = n
            return
        count = 0
        temp = self.root
        while count < pos-1:
            temp = temp.next
            count+=1

        n.next = temp.next
        temp.next = n

    def AddNode(self, val):
        n = Node(val)
        if self.root is None:
            self.root = n
            return
        
        temp = self.root
        while temp.next is not None:
            temp = temp.next

        temp.next = n
    
    def Display(self):
        temp = self.root
        while temp is not None:
            print(temp.val, end="->")
            temp = temp.next

        print("None")


sll = SingleLinkedList()
sll.AddNode(10)
sll.AddNode(20)
sll.AddNode(30)
sll.AddNode(40)
sll.AddNode(50)
sll.InsertNode(100, 3)
sll.InsertNode(200, 5)
sll.AddNode(60)
sll.Display()
