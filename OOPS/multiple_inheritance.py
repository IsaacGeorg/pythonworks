
class Grandparent:
    def m(self):
        print("Grand Parent Class")

class Parent:
    def m(self):
        print("parent class")

class Child(Parent,Grandparent):  # after calling child class, parent class is called-out first and then Grandparent class is called.
    def m3(self):
        print("Child class")

class_instance=Child()
class_instance.m3()
class_instance.m()