from abc import ABC,abstractmethod
class A(ABC):#Abstract Class
    @abstractmethod
    def m1(self):
        None
    @abstractmethod
    def m2(self):
        None
class B(A):#Abstract Class
    def m1(self):
        print("M1")
class C(A):#Concrete Class
    def m1(self):
        print("M1")
    def m2(self):
        print("M2")
    
obj=C()
obj.m1()
obj.m2()

    
