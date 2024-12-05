class Faculty:
    def set_faculty(self,id,name,age,course,experience,salary):
        self.id=id
        self.name=name
        self.age=age
        self.course=course
        self.experience=experience
        self.salary=salary

    def faculty_display(self):
        print(self.name,self.age,self.course)



faculty_instance2=Faculty()
faculty_instance2.set_faculty(3,"Sajay",34,"Python Django",7,45000)
faculty_instance2.faculty_display()