# a dictionary
student = {"mame": "Rolf", "grades": (89, 90, 93, 78, 90)}

# a sequence
def average(sequence):
    return sum(sequence) / len(sequence)


print(average(student["grades"]))
# awkward, better if could do:
# print(student.average())
# needs different code to be able to call the 'average' method


