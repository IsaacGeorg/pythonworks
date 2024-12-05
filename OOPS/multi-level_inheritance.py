
class Grandparent:
    def m1(self):
        print("Grand Parent Class")

class Parent(Grandparent):
    def m2(self):
        print("parent class")

class Child(Parent):
    def m3(self):
        print("Child class")

class_instance=Child()
class_instance.m3()
class_instance.m1()
class_instance.m2()
