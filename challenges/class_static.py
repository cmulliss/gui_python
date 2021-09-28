class ClassTest:
    def instance_method(self):
        print(f"Called instance_method of {self}")

        # how to call it?
        # create a new object.


test = ClassTest()
# to print these would need to use __repr__ method.
test.instance_method()
# or
ClassTest.instance_method(test)


# class, ClassTest, has self as 1st parameter
# all fns inside a class, that use the object self as the 1st parameter, are called instance methods.

# called an instance method because you call it on a class instance
# # instance means an object

# self is the first parameter for instance methods
# cls parameter is the first parameter for class methods
