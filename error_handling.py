# A program to demonstrate error handling.
def divide(x, y):
    try:
        result = x / y
        return result
    except ZeroDivisionError:
        return "Division by zero is not allowed. Choose another number."


if __name__ == "__main__":
    print(divide(3, 4))
    print(divide(3, 0))
