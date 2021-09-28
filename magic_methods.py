class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # gets called when you want to turn your object into a string
    def __str__(self):
        return f"Person {self.name}, {self.age} years old."

    # the goal of the repr method is to be unambiguous, and if possible should return a string that allows us to recreate the original object. Used in debugger.
    def __repr__(self):
        return f"<Person ('{self.name}', {self.age})>"


bob = Person("Bob", 35)
print(bob)

# to test it, can call repr manually, like any other method
print(bob.__repr__())


# methods with 2 underscores each side are 'magic methods, python will call them for you
