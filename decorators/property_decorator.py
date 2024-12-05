
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    @property                               # the decorator is used to change a method to attribute
    def get_age(self):
        print(self.age)
    
    def get_name(self):
        print(self.name)

person_instance=Person("nike",35)
# person_instance.name
person_instance.get_age                     # using the decorator 
person_instance.get_name()