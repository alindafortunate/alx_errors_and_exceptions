def read_students(filename):
    """This function reads students in a file."""
    infile = open(filename, "r")
    students = []
    for line in infile:
        students.append(line)
    infile.close()
    return students


students = read_students("list_of_students.txt")

for student in students:
    print(student)
