
class Stacks:
    def __init__(self, cap):
        self.cap = cap
        self.s = [0] * cap
        self.top = 0

    def Push(self, data):
        if self.IsFull():
            print("Stacks is Full")
            return
        
        self.s[self.top] = data
        self.top += 1
        print(f"{data} is pushed to stack")

    def Pop(self):
        if self.IsEmpty():
            print("Stack is Empty")
            return
        
        self.top -= 1
        data = self.s[self.top]

        print(f"{data} is poped")

    def IsFull(self):
        return self.top == self.cap
    
    def IsEmpty(self):
        return self.top == 0
    
    def Peek(self):
        print(self.s[self.top-1], "is the peek")

    def Display(self):
        for i in range(self.top):
            print(self.s[i], end=" ")
        print()

s = Stacks(5)
s.Push(10)
s.Push(20)
s.Pop()
s.Push(30)
s.Push(50)
s.Peek()
s.Push(60)
s.Push(70)
s.Pop()
s.Push(80)
s.Display()
s.Push(90)
s.Pop()
s.Display()
s.Peek()
