class Student:                                            #creating a class
    def set_student(self,rollNo,name,place,course):       #method1
        self.rollNo=rollNo
        self.name=name                                      #attributes initialization
        self.place=place
        self.course=course

    def studentdisplay(self):                                           #method2
        print(self.rollNo,self.name,self.course)                        #output student details in console


referred_student1=Student()                                 #creating an object with respect to its className
referred_student1.set_student(15,"Anurag","Kaduthuruthy","Python Django")  #input student details 
referred_student1.studentdisplay()                          #a callback for studentdisplay method
referred_student2=Student()
referred_student2.set_student(34,"Irin","Kuravilangad","MERN STACK")
referred_student2.studentdisplay()