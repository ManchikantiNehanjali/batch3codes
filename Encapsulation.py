class Neha:
    def __init__(self,name,age):
        self.__name=name
        self.__age=age
    def get_name(self):
        return self.__name
    def get_age(self):
        return self.__age
    def set_name(self):
        self.__name='Leela'
    def set_age(self):
        self.__age=13
ob=Neha('Neha',15)
print(ob.get_name())
print(ob.get_age())
(ob.set_name())
(ob.set_age())
print(ob.get_name())
print(ob.get_age())
    
