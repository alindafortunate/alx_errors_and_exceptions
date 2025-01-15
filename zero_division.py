# A program to demonastrate the use of *raise* keyword.
import error_handling


def divide(x, y):
    if y == 0:
        raise ZeroDivisionError("Division by zero is not allowed")
    return x / y


print(divide(3, 2))
print(error_handling.divide(3, 4))
