class user():
    __password="password"
    def __init__(self,name,username,email):
        self.name=name
        self.username=username
        self.email=email

    def setPassword(self,new_password):
        self.__password=new_password

    def getPassword(self):
        return self.__password
    
object=user("fred","fr222","fred@gmail.com")
print(object.name)
#print(object.__password)
print(object.email)
print(object.getPassword())
object.setPassword(12345678)
print(object.getPassword())

object2=user("james","jam334","james@gmail.com")
print(object2.email)
print(object2.name)
#print(object2.password)
print(object2.getPassword())