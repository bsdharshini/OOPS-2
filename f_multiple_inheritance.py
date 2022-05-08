#parent class 1
class Car():
    def __init__(self,fuel,tyre):
        self.fuel = fuel
        self.tyre = tyre
    def print_parent_class_attr(self):
        print("parent class 1")
        print(self.fuel," ", self.tyre)
#parent class 2
class truck:
    def __init__(self,fuel,tyre):
        self.fuel = fuel
        self.tyre = tyre
    def print_parent_class_attr(self):
        print("parent class 2")
        print(self.fuel," ", self.tyre)
class petrolVehicle(Car,truck):
    def __init__(self,tyre,fuel):
        super().__init__(tyre,fuel) #didnt use class name and self becaz it has two inherit class name

obj = petrolVehicle(2,'Electric')
obj.print_parent_class_attr() # print class 1 becaus eof order by which passed in child class class 1 comes first

petrolVehicle.__mro__
#returns order = petrol vehicle -> car -> truck

#print mro list
petrolVehicle.mro()