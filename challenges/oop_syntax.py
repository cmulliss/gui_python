class Student:
    def __init__(self):
        self.name = "Rolf"


student = Student()

# calling the class, Student, creates a new empty object, runs the 'init' method and will create empty 'self' and you will be able to modify the name property inside self and give it the value Rolf.
# once the self object contains a name property, Python will give back that self, and Student will become a name for the self thing we created. 
