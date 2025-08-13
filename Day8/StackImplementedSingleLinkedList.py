
class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class StackImplementedSingleLinkedList:
    def __init__(self):
        self.top = None

    def Push(self, val):
        n = Node(val)
        n.next = self.top
        self.top = n

    def Pop(self):
        if self.top is None:
            print("Stack is empty")
            return
        popped = self.top.val
        self.top = self.top.next
        print("popped is", popped)

    def Peek(self):
        if self.top is None:
            print("Stack is empty")
            return
        print(self.top.val, "is Peek value")

    def is_empty(self):
        return self.top is None

    def display(self):
        if self.is_empty():
            print("Stack is empty!")
            return
        current = self.top
        
        while current:
            print(current.val, end=" -> ")
            current = current.next

ss = StackImplementedSingleLinkedList()
ss.Push(10)
ss.Push(20)
ss.Push(30)
ss.Push(40)
ss.Push(50)
ss.Peek()
ss.Pop()
ss.Peek()
ss.Pop()
ss.Peek()
ss.Pop()
ss.Push(60)
ss.Push(70)
ss.Push(80)
ss.display()
