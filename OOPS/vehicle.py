
class Car:
    def __init__(self,name,brand,price):
        self.name=name
        self.brand=brand
        self.price=price

    def display(self):
        print(self.name,self.brand,self.price)

    def __str__(self):                              # __str__  ==> for string representation
        return self.name
    

car_instance1=Car("GT","Porsche","$159300")
car_instance1.display()

print(car_instance1)

