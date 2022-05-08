#1
from ast import Pass


class A():
    def __init__(self,a):
        self.a=a 
class B(A):
    def __init__(self,a,b):
        self.b=b 
c=B('a','b')
print(c.a)

#error: class B has not attr of a 

#2
class A():
    def __init__(self,a):
        self.a=a 
class B(A):
    def __init__(self,a,b):
        super().__init__(a)
        self.b=b 
c=B('a','b')
print(c.a) 
#print 'a'

#3
class A():
    def __init__(self,a):
        self.__a=a 
class B(A):
    def __init__(self,a,b):
        super().__init__(a)
        self.b=b 
    def priB(self):
        print(c.__a,end=' ') 
        print(c.b)

c=B('a','b')
c.priB()
# error because __a is private attr of class A. So need to use like c._A__a

#4
class X:Pass
class Y: Pass
class Z:Pass
class A(X,y): Pass
class B(Y,Z): Pass
class C(B,A,Y):Pass
print(c.mro())
#C>B>A>X>Y>Z>object
