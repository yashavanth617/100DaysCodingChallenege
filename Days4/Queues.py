class Queues:
    def __init__(self, cap):
        self.cap = cap
        self.s = [0] * cap
        self.front = 0
        self.rare = 0
        self.size = 0

    def Enqueue(self, data):
        if self.IsFull():
            print("Queues Is Full")
            return
        self.s[self.rare] = data
        self.rare = (self.rare + 1) % self.cap
        self.size += 1
        print(f"{data} is Enqueued to Queues")

    def Dequeue(self):
        if self.IsEmpty():
            print("Queues Is Empty")
            return
        data = self.s[self.front]
        self.front = (self.front + 1) % self.cap
        self.size -= 1
        print(f"{data} is Dequeue from the Queues")

    def IsFull(self):
        return self.size == self.cap
    
    def IsEmpty(self):
        return self.size == 0
    
    def Peek(self):
        if self.IsEmpty():
            print("Queues Is Empty")
            return
        print(self.s[self.front], "Is Peek")

    def Display(self):
        if self.IsEmpty():
            print("Queues Is Empty")
            return
        i = self.front
        count = 0
        while count < self.size:
            print(self.s[i], end=" ")
            i = (i + 1) % self.cap
            count += 1
        print()

q = Queues(5)
q.Enqueue(10)
q.Enqueue(20)
q.Enqueue(30)
q.Display()
q.Dequeue()
q.Display()
q.Enqueue(40)
q.Enqueue(50)
q.Enqueue(60)
q.Display()
q.Peek()
q.Enqueue(70)
q.Display()
q.Enqueue(80)
q.Dequeue()
q.Dequeue()
q.Enqueue(90)
q.Display()
q.Enqueue(100)
q.Display()
