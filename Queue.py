class Queue():
    def __init__(self,max):
        self.max=max
        self.queue=[]
    def enqueue(self,add):
        if self.size()<self.max:
            self.queue.append(add)
        else:
            print("Queue is full.")
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty.")
        else:
            return self.queue.pop(0)
    def display(self):
        print(self.queue)

    def front(self):
        if not self.is_empty():
            return self.queue[0]
        
    def rear(self):
        if not self.is_empty():
            return self.queue[-1]
        
    def size(self):
        return len(self.queue)
    
    def is_empty(self):
        if self.queue==0:
            return True
        else:
            return False
    
a=Queue(3)
a.enqueue(9)
a.display()

a.enqueue(99)
a.display()

a.enqueue(21)
a.display()
print(a.front())
print(a.rear())

a.enqueue(0)
a.display()

a.dequeue()
a.display()
print(a.front())
print(a.rear())

a.dequeue()
a.display()

a.dequeue()
a.display()

a.dequeue()
a.display()