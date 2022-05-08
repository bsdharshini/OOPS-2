#parent class
class Vehicle:
    def __init__(self,fuel,model):
        self.__fuel = fuel #private attr
        self.model = model
    #private method
    def __print_value(self):
        print("parent private method")
        print(self.__fuel)

#child class
class Car(Vehicle):

    # must add parent class instance attr also
    def __init__(self,fuel,model,a_c,sunroof):
        Vehicle.__fuel = fuel #Base class private attr
        Vehicle.model = model # Base class attr
        self.a_c=a_c
        self.sunroof = sunroof

    # to access parent class private attr
    def print_parent_private_attr(self):
        print(Vehicle.__fuel," ", Vehicle.model)

    # to access parent class private method
    def show_parent_private_method(self):
        self._Vehicle__print_value()
        #why self? To create an instance of parent class


obj = Car('Petrol',2020,True,False)
print(obj.__dict__) # will not show parent class attr
obj.print_parent_class_attr()
print(obj.fuel) # print fuel value
    
print(obj.__fuel)#error
print(obj.fuel)#error
obj.print_parent_private_attr() # print value
obj.show_parent_private_method() # print parent method value

# if show_parent_private_method, print_parent_private_attr is also private method then use like this

#obj._Car__print_parent_private_attr()
#obj._Car__show_parent_private_method()