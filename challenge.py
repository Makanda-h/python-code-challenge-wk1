# function that takes in two numbers and returns their sum
def add_numbers(num1, num2) :
    return num1+num2

# function that checks if anumber is even and returns true if it is, false otherwise
def is_even(num):
    return num % 2 == 0

# function that takes in a string and returns the string reversed
def reverse_string(string):
    return string[::-1]

# function that takes in a string and returns the number of vowels in the string
def count_vowels(string):
    vowels = ["a","e","i","o","u"]
    count = 0
    for char in string.lower():
        if char in vowels:
            count +=1
    return count

# function that calculates the factorial of a number
def calculate_factorial(n):
    factorial = 1
    for i in range(1, n+1):
        factorial *= i
    return factorial

# function that uses a decorator function to print "Decorator Applied" before the function is called
def apply_decorator(func):
    def decorator_func(*args, **kwargs):
        print("Decorator Applied")
        return func(*args, **kwargs)
    return decorator_func

def sort_by_age(list_of_tuples):
# Sort the list using the second element [1] of each tuple assuming it is the age
# lambda is an anonymous function that specifies the sorting key
    return sorted(list_of_tuples, key=lambda x: x[1]) 

def merge_dicts(dict1, dict2):
    # create a copy of dict1 to avoid modifying the original dictionary
    merged = dict1.copy()
    # iterate over the second dictionary and add the values to the merged dictionary
    # if the key already exists, add the values together
    # if the key does not exist, add the key-value pair to the merged dictionary
    # return the merged dictionary
    for key, value in dict2.items():  
        if key in merged:
            merged[key] += value
        else:
            merged[key] = value
    return merged

class Car:
    # Create a class Car with attributes make, model and year
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        # Create a method display_info that prints the year, make and model of the car
    def display_info(self):
        print(f"Model: {self.model}, Make: {self.make}, Year: {self.year}")