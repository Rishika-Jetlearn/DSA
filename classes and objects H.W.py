class bank_account():
    def __init__(self,name,age,password):
        self.money=0
        self.name=name
        self.age=age
        self.password=password

    def set_new_password(self,new):
        self.password=new
    
    def getPassword(self):
        return self.password
    
    def add_money(self,added_money):
        self.money=self.money+added_money

    def chack_balance(self):
        print(self.money)
        return self.money
    
    def withdraw_money(self,withrawed_money):
        self.money=self.money-withrawed_money
#new user
person=bank_account("hidia","99","hidia99")
print(person.name)
print(person.age)
print(person.password)

person.chack_balance()
person.add_money(20)
person.chack_balance()

person.withdraw_money(10)
person.chack_balance()
#after hidia birthday

person.set_new_password("hidia100")
print(person.getPassword())
