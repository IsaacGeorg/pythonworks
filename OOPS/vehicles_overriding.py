
class Parent:

    def vehicles(self,bikes):
        self.bikes=["passion pro","activa"]
        return self.bikes
    
class Child(Parent):

    def vehicles(self,bikes):
        self.bikes=super().vehicles()
        self.bikes.append("hunter")
        return self.bikes

child_instance=Child()
child_instance.vehicles()
