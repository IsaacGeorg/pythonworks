
class Student:
    id:int        #attributes (OPTIONAL)
    name:str
    age:int
    course:str

    def set_student(self,id,name,age,course):      #method1
        self.id=id                #student class attributes initialization
        self.name=name
        self.age=age
        self.course=course

    def display(self):              #method2
        print(self.name,self.age)           #displaying student class details


# Creating object of class Student
# referenceName=className   

# Here referenceName => studentinstance1   &  className => Student

student_instance1=Student()

student_instance2=Student()

student_instance1.set_student(1009,"George",34,"Law")

student_instance1.display()





# Employee
# Student