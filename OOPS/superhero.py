
class Superhero:
    def __init__(self,name,suit):
        self.name=name
        self.suit=suit
    def __str__(self):
        return self.name
    
class Spiderman(Superhero):
    def __init__(self,name,suit):
        super().__init__(name,suit)
    def super_power(self):
        print("Web-shooting","Crawling","Combat-damage power","stealth")

class Minnalmurali(Superhero):
    def __init__(self,name,suit):
        super().__init__(name,suit)
    def super_power(self):
        print("Minnal","levitation","flying")
    
minnal_instance=Minnalmurali("Minnal-Murali","Murali suit")
print(minnal_instance)