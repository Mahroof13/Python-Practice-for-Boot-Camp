# NameError
def print_variable():
    try:
        print(my_variable)
    except NameError as ne:
        print(f"Caught a NameError: {ne}")

print_variable()

# TypeError
def divide_numbers(a, b):
    try:
        result = a / b
        print(f"The result of the division is: {result}")
    except TypeError as te:
        print(f"Caught a TypeError: {te}")

divide_numbers('10', 2)  # This will raise a TypeError

# ValueError
try:
    int("abc")  # This will raise a ValueError
except ValueError as ve:
    print(f"Caught a ValueError: {ve}")

# ZeroDivisionError
try:
    result = 10 / 0  # This will raise a ZeroDivisionError
except ZeroDivisionError as zde:
    print(f"Caught a ZeroDivisionError: {zde}")    

# KeyError
try:
    my_dict = {'a': 1}
    print(my_dict['b'])  # This will raise a KeyError
except KeyError as ke:
    print(f"Caught a KeyError: {ke}")

# IndexError
try:
    my_list = [1, 2, 3]
    print(my_list[5])  # This will raise an IndexError
except IndexError as ie:
    print(f"Caught an IndexError: {ie}")
