def divide(num1, num2):
    try:
        result = num1 / num2
        print(f"{num1} divided by {num2} is: {result}")
    except ZeroDivisionError:
        print(f"Division by zero is not allowed.")


divide(3, 4)
divide(3, 0)
divide(0, 4)
