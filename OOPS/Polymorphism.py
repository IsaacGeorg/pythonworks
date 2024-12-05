
# Polymorphism (many forms)
# method overloading
# method overriding

class Operations:                       # (same method name, different number of paramaters)

    def add(self,num1,num2):
        print(num1+num2)

    def add(self,num1,num2,num3):
        print(num1+num2+num3)

obj=Operations()
obj.add(4,8,2)
obj.add(4,3)                        # method overloading error


# To avoid this error, *args is used


# Overriding
# Rules:
# 1.min 2 class
# 2.must be inherited from parent
# 3.the mehods must have same signature


class Parent:
    def mobile(self):
        print("nokia")

class Child(Parent):
    def mobile(self):
        print("iphone")

child_instance=Child()
child_instance.mobile()

