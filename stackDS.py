class Stack():
    def __init__(self,max):
        self.max=max
        self.stack=[]
    #adding
    def push(self,item):
        if self.size()<self.max:
            self.stack.append(item)
        else:
            print("stack is full")
    
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            print("Stack is empty")

    def top(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            print("stack is empty")
    
    def size(self):
        return len(self.stack)

    def is_empty(self):
        if self.size()==0:
            return True
        else:
            return False

    def display(self):
        print(self.stack)
    
    def check_item(self,item):
        if item in self.stack:
            return True
        else:
            return False

"""object= Stack(3)

object.push("a")
object.display()

object.push("b")
object.display()

object.push("c")
object.display()

print(object.top())

object.push("d")
object.display()

object.pop()
object.display()

print(object.pop())
object.display()

object.pop()
object.display()

object.pop()
object.display()"""
