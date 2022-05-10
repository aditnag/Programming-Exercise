def value_error():
    try:
        x = int(input("What's the value for x? "))

    except ValueError:
        print("x is not an integer!")

    # print(f"x is {x}") will cause ValueError in line 3
    # as int fn will throw error for string value and x will not be updated
    else:
        print(f"x is {x}")


# This function will go on until user inputs a valid integer
def value_error_new_solution():
    while True:
        try:
            x = int(input("What's the value for x? "))
        except ValueError:
            print("x is not an integer")
        else:
            break
    print(f"x is {x}")


def main():
    x = int(input("Enter your choice 1 or 2: "))
    if x == 1:
        value_error()
    elif x == 2:
        value_error_new_solution()
    else:
        print("Invalid choice!")


if __name__ == "__main__":
    main()
