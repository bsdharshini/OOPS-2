class o():
    def __init__(self,radius):
        self.radius = radius
i = o(3)
print(i)
# prints the class object and address

#we can override this ith __str__
class o():
    def __init__(self,radius):
        self.radius = radius
    def __str__(self):
        return ("This is overridden message")
i = o(3)
print(i)

#print new message