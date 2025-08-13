
class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class SingleLinkedList:
    def __init__(self):
        self.root = None

    def AddNode(self,val):
        n = Node(val)
        if self.root is None:
            self.root = n
            return
        
        temp =self.root
        while temp.next is not None:
            temp =temp.next
        temp.next = n
        temp = n

    def DisplayForward(self):
        temp = self.root
        while temp is not None:
            print(temp.val, end="->")
            temp = temp.next
        print("None")

    def DisplayReverse(self):
        temp = self.root
        l = []
        while temp is not None:
            l.append(temp.val)
            temp = temp.next
        while len(l) > 0:
            print(l.pop(), end="->")
        print("None")


sll = SingleLinkedList()
sll.AddNode(10)
sll.AddNode(20)
sll.AddNode(30)
sll.AddNode(40)
sll.AddNode(50)
sll.AddNode(60)
sll.DisplayForward()
sll.DisplayReverse()
