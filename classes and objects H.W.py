class bank():
    def __init__(self,name,age,password):
        self.name=name
        self.age=age
        self.password=password
    def set_new_password(self,new):
        self.password=new
    
    def getPassword(self):
        return self.password
    

#new user
person1=bank("hidia","99","hidia99")
print(person1.name)
print(person1.age)
print(person1.password)

#after hidia birthday

person1.set_new_password("hidia100")
print(person1.getPassword())

