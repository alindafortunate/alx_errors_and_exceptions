class ValueTooHighError(Exception):
    """Raise an error if the the number is too high."""

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


try:
    number = int(input("Enter a number below 100: "))
    if number > 100:
        raise ValueTooHighError("Value greater 100, choose a value below.")
except (
    ValueTooHighError
) as e:  # We use as e to know the exact error happening, or the message about the error.
    print(f"{e}")
else:
    print(f"Your number is: {number}")
