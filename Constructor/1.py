class Student:
    def __init__(self, name,age,grade):
        self.name = name
        self.age = age
        self.grade = grade

#creating objacts
student1 = Student('pradip',26,'A++')
student2 = Student('Kalpesh',50, 'B+')

print(student1.name, student1.age, student1.grade)
print(student2.name, student2.age, student2.grade)
"""
1- default constructor (self)
2- Parameterized constructor,(self,name, age)
3- constructor with default values,(self, name ="unknown",age = 0)
"""