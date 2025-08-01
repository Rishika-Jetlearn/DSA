class Queue():
    def __init__(self,max):
        self.max=max
        self.queue=[]
    def enqueue(self,add):
        if len(self.queue)<self.max:
            self.queue.append(add)
        else:
            print("Queue is full.")
    def dequeue(self):
        if len(self.queue)==0:
            print("Queue is empty.")
        else:
            return self.queue.pop(0)
    def display(self):
        print(self.queue)

a=Queue(3)
a.enqueue(9)
a.display()

a.enqueue(99)
a.display()

a.enqueue(21)
a.display()

a.enqueue(0)
a.display()

a.dequeue()
a.display()

a.dequeue()
a.display()

a.dequeue()
a.display()

a.dequeue()
a.display()