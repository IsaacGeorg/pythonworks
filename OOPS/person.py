
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display_person_info(self):
        print(self.name,self.age)

class Employee:
    def __init__(self,emp_id,salary):
        self.emp_id=emp_id
        self.salary=salary
    def display_employee_info(self):
        print(self.emp_id,self.salary)


class Manager(Person,Employee):
    def __init__(self,name,age,emp_id,salary,department):
        Person.__init__(self,name,age)
        Employee.__init__(self,emp_id,salary)
        self.department=department

    def display_manager(self):
        self.display_person_info()
        self.display_employee_info()
        print(self.department)
    

class_instance=Manager("Akhilesh",27,"E101",25000,"hr")
class_instance.display_manager()