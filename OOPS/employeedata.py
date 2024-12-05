
class Employee:
    def set_employee(self,empid,name,age,gender,department,salary):
        self.empid=empid
        self.name=name
        self.age=age
        self.gender=gender
        self.department=department
        self.salary=salary
    
    def display(self):
        print(self.age,self.department,self.salary)


employee_1=Employee()
employee_1.set_employee(101,"Harrison Wells",36,"Male","Research & Development",65000)
employee_2=Employee()
employee_2.set_employee(108,"Cisco Ramo",27,"Male","Science",80000)

employee_1.display()
employee_2.display()
