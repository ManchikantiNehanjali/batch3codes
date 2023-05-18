#Overloading in python is done by two ways by using default arguments,*args and **kwargs arguments
class A:
    def m1(self,*args):
        if len(args)==1:
            print("args len 1")
        elif len(args)==2:
            print("args len 2")
obj=A()
obj.m1(1,2)
obj.m1(1)

class A:
    def m1(self,a=None,b=None):
        print(a,b)
obj=A()
obj.m1()
obj.m1(1)
obj.m1(1,2)
