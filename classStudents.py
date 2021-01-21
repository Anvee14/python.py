class Student(object):
    def __init__(self, name, age, gender, level, grades=None):
        self.name = name
        self.age = age
        self.gender = gender
        self.level = level
        self.grades = grades or {}

    def setGrade(self, course, grade):
        self.grades[course] = grade

    def getGrade(self, course):
        return self.grades[course]

    def getGPA(self):
        return sum(self.grades.values())/len(self.grades) , self.name,self.age,self.level
        


# Define some students
john = Student("John", 12, "male", 6, {"physics": 4,"math":8})
jane = Student("Jane", 12, "female", 6, {"math": 3.5})

# Now we can get to the grades easily
print(john.getGPA())
print(jane.getGPA())
