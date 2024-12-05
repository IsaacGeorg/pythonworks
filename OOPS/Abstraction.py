# abc==> abstract base class
# implementation details are hidden

# no definitions

# 
from abc import ABC,abstractmethod

class Car(ABC):

    @abstractmethod
    def start(self):
        pass
    
    @abstractmethod
    def accelerate(self):
        pass
    
    @abstractmethod
    def brake(self):
        pass

    @abstractmethod                     # @abstractmethod is a decorator
    def stop(self):
        pass
    
    @abstractmethod
    def gear_shift(self):
        pass

class Mercedenz_Benz(Car):

    def start(self):
        print("Starting")

    def brake(self):
        print("brake method")

    def accelerate(self):
        print("Acceleration")

    def gear_shift(self):
        print("Shifting")

    def stop(self):
        print("Stopped!!")

benz_instance=Mercedenz_Benz()
benz_instance.start()
benz_instance.gear_shift()
benz_instance.accelerate()
