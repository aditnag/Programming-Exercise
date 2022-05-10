def value_error():
    try:
        x = int(input("What's the value for x? "))

    except ValueError:
        print("x is not an integer!")

    else:
        print(f"x is {x}")


value_error()
