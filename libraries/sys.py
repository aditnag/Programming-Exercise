import sys


# try:
#     print("Hello, my name is ", sys.argv[1])
# except IndexError:
#     print("Argument missing")

# Error Handling
if len(sys.argv) < 2:
    sys.exit("Too few args")
elif len(sys.argv) > 2:
    sys.exit("Too many args")
# else:
#     print("Hello, my name is ", sys.argv[1])

print("Hello, my name is ", sys.argv[1])