#parent class
class Vehicle:
    current_year = 2022
    base_price = 10000
    def __init__(self,fuel,model):
        self.__fuel = fuel #private attr
        self.model = model
    #private method
    def __print_value(self):
        age =Vehicle.current_year -self.model
        print("parent class method")
        return Vehicle.base_price * (1/age)
class Car(Vehicle):

    # must add parent class instance attr also
    def __init__(self,fuel,model,a_c,sunroof):
        #define super fn with class name and self
        super(Car,self).__init__(fuel,model)
        self.a_c=a_c
        self.sunroof = sunroof

    # method overriding - replace parent default method
    def __print_value(self):
        Vehicle.base_price = 5000
        age =Vehicle.current_year -self.model
        print("Child class method")
        print(self.a_c)
        return Vehicle.base_price * (1/age)
obj = Car("Petrol",2020,True,False)
print(obj._Car__print_value()) # print child method

parentObj = Vehicle("Diesel",2019)
print(parentObj._Vehicle__print_value())