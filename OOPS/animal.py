

class Animal:

    def __init__(self,name,species):
        self.name=name
        self.species=species
    
    def __str__(self):
        return self.name

class Lion(Animal):
    def __init__(self, name, species):
        super().__init__(name, species)

    def sound(self):
        print("Lion ==> Roar")

class Cat(Animal):
    def __init__(self,name,species):
        super().__init__(name,species)

    def sound(self):
        print("Cat ==> Meow")

animal_instance1=Lion("Simba","Carnivorous")
print(animal_instance1)
animal_instance1.sound()
