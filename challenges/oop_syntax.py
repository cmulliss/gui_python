class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average(self):
        return sum(self.grades) / len(self.grades)


student = Student("Bob", (90, 90, 93, 78, 90))
student2 = Student("Rolf", (100, 89, 93, 78, 100))
print(student.name)
print(student.grades)
print(student2.name)
print(student2.grades)
# uses the object that was created, calling the Student class, then the average fn, and put the student object in.
# class fn object
print(Student.average(student))
# or better, get it to do the conversion for you, call the average method on the object itself:
print("Student average", student.average())
print("Student2 average", student2.average())

# calling the class, Student, creates a new empty object, runs the 'init' method and will create empty 'self' and you will be able to modify the name property inside self and give it the value Rolf.
# once the self object contains a name property, Python will give back that self, and 'student' will become a name for the self thing we created.
# so we are using this class, Student, through the init method to create an object and assign the name property to inside the object to the string Rolf. Then that object is what becomes the value for our 'student' variable.

# you call a class, the init method runs, and what you get back is the object you created.

# (90, 90, 93, 78, 90)
