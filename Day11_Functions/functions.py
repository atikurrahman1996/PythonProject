# Defining a Function:
# is a reusable block of code or programming statements designed to perform a certain task.
# To define or declare a function, Python provides the def keyword.
# The function block of code is executed only if the function is called or invoked.

def generate_full_name():
    first_name = 'AR'
    last_name = 'ARIYAN'
    space = ' '
    full_name = first_name + space + last_name
    print(full_name)


generate_full_name()  # calling a function


def add_two_numbers():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    print(total)


add_two_numbers()


# Function Returning a Value

def generate_full_name():
    first_name = 'Atik'
    last_name = 'Ariyan'
    space = ' '
    full_name = first_name + space + last_name
    return full_name


print(generate_full_name())


def add_two_numbers():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    return total


print(add_two_numbers())


# Functions with single parameter

def greetings(name):
    message = name + ', welcome to Python for Everyone!'
    return message


print(greetings('AR'))


def square_number(x):
    return x * x


print(square_number(2))


def area_of_circle(r):
    PI = 3.14
    area = PI * r ** 2
    return area


print(area_of_circle(10))


# Two parameters

def generate_full_name(first_name, last_name):
    space = ' '
    full_name = first_name + space + last_name
    return full_name


print('Full Name is: ', generate_full_name('AR', 'ATIK'))


def sum_two_numbers(num_one, num_two):
    sum = num_one + num_two
    return sum


print('Sum of two numbers: ', sum_two_numbers(1, 9))


def calculate_age(current_year, birth_year):
    age = current_year - birth_year
    return age

print(calculate_age(2025, 1996))

#Function with Default Parameters

def greetings (name = 'Jahan'):
    message = name + ', welcome to Python for Everyone!'
    return message
print(greetings()) #Jahan
print(greetings('Israt')) #Israt

def generate_full_name (first_name = 'AR', last_name = 'Ariyan'):
    space = ' '
    full_name = first_name + space + last_name
    return full_name

print(generate_full_name())
print(generate_full_name('Israt','Jahan'))