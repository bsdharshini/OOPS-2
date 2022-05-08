#parent class
class Vehicle:
    def __init__(self,fuel,model):
        self.fuel = fuel
        self.model = model
#child class
class Car(Vehicle):
    # must add parent class instance attr also
    def __init__(self,fuel,model,a_c,sunroof):
        Vehicle.fuel = fuel
        Vehicle.model = model
        self.a_c=a_c
        self.sunroof = sunroof
    # to access parent class attr
    def print_parent_class_attr(self):
        print(Vehicle.fuel," ", Vehicle.model)

obj = Car('Petrol',2020,True,False)
print(obj.__dict__) # will not show parent class attr
obj.print_parent_class_attr()
print(obj.fuel) # print fuel value
    
