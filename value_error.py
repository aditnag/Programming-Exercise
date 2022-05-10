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
            # x = int(input("What's the value for x? "))
            return int(input("What's the value for x? "))
        #   break here will also work
        except ValueError:
            # print("x is not an integer")
            pass # to re-prompt the user again and again
        # else:
            # break
            # return x  # return is stronger than break, as it will not only break from the code but also return the value
    # print(f"x is {x}")
    # return x


def main():
    while True:
        x = int(input("Enter your choice 1 or 2: "))
        if x == 1:
            value_error()
            break
        elif x == 2:
            # value_error_new_solution()
            num = value_error_new_solution()
            print(f"x is {num}")
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
