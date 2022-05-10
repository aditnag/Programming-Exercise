def value_error():
    try:
        x = int(input("What's the value for x? "))

    except ValueError:
        print("x is not an integer!")

    # print(f"x is {x}") will cause ValueError in line 3
    # as int fn will throw error for string value and x will not be updated
    else:
        print(f"x is {x}")


value_error()
