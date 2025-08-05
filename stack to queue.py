import stackDS

class stack_queue():
    def __init__(self,max):
        self.queue=stackDS.Stack(max)
        self.temp=stackDS.Stack(max) 
        self.max=max
    def dequeue(self):
        if self.queue.is_empty():
            print("Error, Queue is empty")
        else:
            return self.queue.pop()
        

    def enqueue(self,item):
        if self.queue.size()<self.max:
            while not self.queue.is_empty():
                taken_out=self.queue.pop()
                self.temp.push(taken_out)
            
            
            self.queue.push(item)

            while not self.temp.is_empty():
                back_in=self.temp.pop()
                self.queue.push(back_in)
        else:
            print("Queue is full.")
        

    def display(self):
        self.queue.display()
a=stack_queue(3)
a.enqueue(9)
a.display()

a.enqueue(99)
a.display()

a.enqueue(21)
a.display()


a.enqueue(10)
a.display()

a.dequeue()
a.display()

a.dequeue()
a.display()

a.dequeue()
a.display()

a.dequeue()
a.display()