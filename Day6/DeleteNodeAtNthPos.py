class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class SingleLinkedList:
    def __init__(self):
        self.root = None

    def DeleteNode(self, pos):
        if self.root is None:
            print("Node is empty")
            return
        if pos < 1:
            print("Position should be greater than 0")
            return  
        if pos == 1:
            self.root = self.root.next
            return      
        count = 1
        temp = self.root        
        while count < pos - 1 and temp is not None:
            temp = temp.next
            count += 1
        if temp is None or temp.next is None:
            print("Position out of range")
            return
        temp.next = temp.next.next


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
sll.Display()
sll.DeleteNode(3)
sll.DeleteNode(4)
sll.AddNode(60)
sll.Display()
