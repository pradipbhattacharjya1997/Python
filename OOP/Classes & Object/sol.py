class Student:
    def set_details(self,name, marks):
        self.name = name
        self.marks = marks
        
Student1 =Student()
Student1.set_details('Udit',95)
print(Student1.name,Student1.marks) 