# Reading a file line by line is ideal for large files while read() is for small files.
def openfile(filename):
    """This functions open a file and reads the file contents by a forloop."""
    try:
        if filename == filename:
            file = open(filename, "r")
            for line in file:
                print(line.strip())
        file.close()
        print()
        print("#File closed.")
    except FileNotFoundError:
        print(f"Error, file doesn't exit.")


openfile("list_of_students.txt")
# openfile("zero_division.py")
