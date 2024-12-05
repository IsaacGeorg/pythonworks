
class Shipping:

    def calculate_shipping_cost(self,weight):
        print(weight*5)

class Express_shipping(Shipping):
    def calculate_shipping_cost(self,weight):
        print(weight*20)

class Standard(Shipping):
    def calculate_shipping_cost(self,weight):
        print(weight*10)

ship_instance=Standard()
ship_instance.calculate_shipping_cost(540)
ship_instance1=Express_shipping()
ship_instance1.calculate_shipping_cost(39)


# Abstraction
    # Hiding Implementation Details