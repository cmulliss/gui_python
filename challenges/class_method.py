class ClassTest:
    def instance_method(self):
        print(f"Called instance_method of {self}")

    @classmethod
    def class_method(cls):
        print(f"Called class_method of {cls}")


# because its a class method, not an instance method, no longer need an instance
# test = ClassTest, instead can do:
ClassTest.class_method()
# cls is ClassTest and python will automatically pass it in
# ClassTest.class_method(ClassTest)


@staticmethod
def static_method():
    print("Called static method")


# cls refers to the class itself

# cls parameter is the first parameter for class methods
# self is the first parameter for instance methods

# Instead of accepting a self parameter, class methods take a cls parameter that points to the class, and not the object instance, when the method is called. Since the class method only has access to this cls argument, it can’t modify object instance state. That would require access to self . However, class methods can still modify class state that applies across all instances of the class.
