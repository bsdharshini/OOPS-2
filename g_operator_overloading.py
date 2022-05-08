class one():
    def __init__(self,price):
        self.price =price
    
    #operatore overloading fn
    def __add__(self,other):
        return self.price+other.price
obj = one(100)
obj1 = one(200)
print(obj+obj1) #300

# without operator overloading we will get error because object cannot be added
#llrly we can do sub, multiplication, divide, pow and so on 