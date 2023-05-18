class A:
    def Fruit(self):
        print("Mango")
class B(A):
    def Fruit(self):
        print("Apple")
        super().Fruit()
ob=B()
ob.Fruit()
