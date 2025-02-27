class ValueTooHighError(Exception):
    """Raise an error if value is above 100."""

    def __init__(self, message="Error value is above 100."):
        self.message = message

    def __str__(self):

        return f"{self.message}"


try:
    number = int(input("Enter a value below 100: "))
    if number >= 100:
        raise ValueTooHighError
except ValueTooHighError as e:
    print(e)
else:
    print(f"The number is: {number}")
