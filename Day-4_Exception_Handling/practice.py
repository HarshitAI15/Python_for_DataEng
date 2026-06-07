# import os,csv,requests
# try:
#     number = int("5r")
#     print("Successfully converted to int")
# except ValueError as e:
#     print(f"ValueError: {e}")
# print("above code executed")


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b

try:
    result = divide(10, 1)
    print(f"Result: {int(result)}")
except ValueError as e:
    print(f"Error: {e}")