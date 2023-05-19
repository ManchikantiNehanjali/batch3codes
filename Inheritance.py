#Single inheritance

class A:
    def show(self):
        print("Show")
class B(A):
    def show1(self):
        print("Show1")
obj=B()
obj.show1()
obj.show()

#Multilevel Inheritance

class Grandparent:
    def show(self):
        print("Show")
class Parent(Grandparent):
    def show1(self):
        print("Show1")
class Child(Parent):
    def show2(self):
        print("Show2")
obj=Child()
obj.show()
obj.show1()
obj.show2()

#Hierarchial Inheritance

class Parent:
    def show(self):
        print("show")
class child1(Parent):
    def show1(self):
        print("show1")
class child2(Parent):
    def show2(self):
        print("show2")
ob1=child1()
ob1.show1()
ob1.show()
ob2=child2()
ob2.show2()
ob2.show()

#Multiple Inheritance

class Father:
    def show(self):
        print("show")
class Mother:
    def show1(self):
        print("show1")
class child(Father,Mother):
    def show2(self):
        print("Child")
ob=child()
ob.show2()
ob.show1()
ob.show()
