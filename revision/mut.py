a = []
b = a

# these give the same location in memory
print(id(a))
print(id(b))

""" gives
140342475815296
140342475815296
"""
a.append(35)

print(a)
print(b)

""" gives
[35]
[35]
"""

a = "hello "
b = a

a += "world"  # same as a = a +"world"
print(a)
print(b)

"""
gives
hello world
hello 

because reassigning a into new string, but b staying the same
"""
