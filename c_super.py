#super method

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
        #define super fn with class name and self
        super(Car,self).__init__(fuel,model)
        self.a_c=a_c
        self.sunroof = sunroof
obj = Car('Diesel',2020,True,False)
print(obj.model) #2020
print(obj.__dict__) # print both parent and child class instance attr
obj._Vehicle__print_value() #print method value
# calling with Vehicle class name because it is private method. 
#If it is public methid then call only parent method name