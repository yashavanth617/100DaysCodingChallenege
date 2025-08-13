class Node:
    def __init__(self, val):
        self.val = val
        self. next = None

class SingleLinkedList:
    def __init__(self):
        self.root = None
    
    def AddNode(self, val):
        n = Node(val)
        if self.root is None:
            self.root = n
            return
        
        temp = self.root
        while temp.next is not None:
            temp = temp.next
        temp.next = n
    
    def DeleteNthNode(self, n):
        dummy = Node(0)
        dummy.next = self.root
        first = dummy
        second = dummy
        
        
        for _ in range(n + 1):
            if first is None:
                print("Invalid position")
                return
            first = first.next
        
        
        while first:
            first = first.next
            second = second.next
        
       
        second.next = second.next.next
        
        self.root = dummy.next
    
    def Display(self):
        temp = self.root
        while temp is not None:
            print(temp.val, end="->")
            temp =temp.next
        print("None")

sll = SingleLinkedList()
sll.AddNode(10)
sll.AddNode(20)
sll.AddNode(30)
sll.AddNode(40)
sll.AddNode(50)
sll.Display()
sll.DeleteNthNode(1)
sll.Display()
