def open_and_read_file(filename):
    try:
        file = open(filename)
        content = file.read()
        print(content)
        file.close()

    except FileNotFoundError:
        print("Sorry, file doesn't exit")


open_and_read_file("custom_error.py")
