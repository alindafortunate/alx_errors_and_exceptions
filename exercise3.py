# Exercise 2: File Handling with FileNotFoundError

# Instructions:

# Write a program that attempts to open and read data from a file specified by the user.
# Handle the FileNotFoundError exception to provide a meaningful message if the file does not exist.


class ValueTooHighError(Exception):
    """Raise an error if value is above 100."""

    def __init__(self, message="Error value is above 100."):
        self.message = message

    def __str__(self):

        return f"{self.message}"


number = int(input("Enter a value below 100: "))
if number >= 100:
    raise ValueTooHighError
