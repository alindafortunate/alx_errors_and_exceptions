# A program to demonstrate the use of finally.
try:
    with open("zero_division.py", "r") as file:
        content = file.read()
        print(f"{file.name}: \n{content}")
except FileNotFoundError:
    print(f"File doesn't exist, check the spelling.")
finally:
    print("#Thank you for using our service.")
