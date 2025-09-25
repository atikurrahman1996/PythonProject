#Function as a Parameter
def higher_order_function(f, lst):  # function as a parameter
    summation = f(lst)
    return summation

# Passing built-in sum function and a list
result = higher_order_function(sum, [1, 2, 3, 4, 5])
print(result)


#Function as a Return Value

def square(x):          # a square function
    return x ** 2

def cube(x):            # a cube function
    return x ** 3

def absolute(x):        # an absolute value function
    if x >= 0:
        return x
    else:
        return -x

def higher_order_function(shape): # a higher order function returning a function
    if shape == 'square':
        return square
    elif shape == 'cube':
        return cube
    elif shape == 'absolute':
        return absolute

result = higher_order_function('square')
print(result(3))       # 9
result = higher_order_function('cube')
print(result(3))       # 27
result = higher_order_function('absolute')
print(result(-3))      # 3


#Python Closures
#Python allows a nested function to access the outer scope of the enclosing function. This is is known as a Closure.

#Example:

def add_ten():
    ten = 10
    def add(num):
        return num + ten
    return add

closure_result = add_ten()
print(closure_result(5))  # 15
print(closure_result(10))  # 20


#Creating Decorators
#To create a decorator function, we need an outer function with an inner wrapper function.

#Example:
# Normal function
def greeting():
    return 'Welcome to Python'
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper
g = uppercase_decorator(greeting)
print(g())        # WELCOME TO PYTHON

## Let us implement the example above with a decorator

'''This decorator function is a higher order function
that takes a function as a parameter'''
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

@uppercase_decorator
def morning():
    return 'Welcome to Python'
print(morning())   # WELCOME TO PYTHON