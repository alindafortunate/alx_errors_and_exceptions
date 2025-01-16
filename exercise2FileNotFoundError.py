# Reading a file line by line is ideal for large files while read() is for small files.

# Exercise 2: File Handling with FileNotFoundError

# Instructions:


# Write a program that attempts to open and read data from a file specified by the user.
# Handle the FileNotFoundError exception to provide a meaningful message if the file does not exist.


def openfile(filename):
    """This functions open a file and reads the file contents by a forloop."""
    try:
        if filename:
            file = open(filename, "r")
            for line in file:
                print(line.strip())
        file.close()
        print()
        print("#File closed.")
    except FileNotFoundError:
        print(f"Error, file doesn't exit.")


# openfile("list_of_students.txt")
# openfile("zero_division.py")


def read_files(files):
    """Reads and prints the content of multiple files."""
    for filename in files:
        try:
            with open(filename, "r") as file_obj:
                content = file_obj.readlines()
                print(f"Contents of {filename}:\n{''.join(content)}\n")
        except FileNotFoundError:
            print(f"File '{filename}' doesn't exist.\n")


read_files(["error_handling.py", "custom_error.py", "students.txt"])


def read_files(files):
    """Reads and prints the content of multiple files."""
    for filename in files:
        try:
            with open(filename, "r") as file_obj:
                content = file_obj.readlines()
                print(f"Contents of {filename}:\n{''.join(content)}\n")
        except FileNotFoundError:
            print(f"File '{filename}' doesn't exist.\n")


read_files(["error_handling.py", "custom_error.py", "students.txt"])
