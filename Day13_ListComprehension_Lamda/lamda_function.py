#Lambda function is a small anonymous function without a name. It can take any number of arguments, but can only have one expression.
# Lambda function is similar to anonymous functions in JavaScript
#To create a lambda function we use lambda keyword followed by a parameter(s), followed by an expression
from Day3_Operators.operators import multiply


#Example:

# Without Lamda Function
def add_two_nums(a, b):
    return a + b
print(add_two_nums(2, 3))     # 5

# With Lamda Function

add_two_nums = lambda a, b: a + b
print(add_two_nums(2,3))    # 5

add_three_nums = lambda a, b, c: a+b+c
print(add_three_nums(5, 5,5)) #25

# Lambda function to multiply three numbers
multiply_three_nums = lambda a, b, c: a * b * c
print(multiply_three_nums(5, 5, 5)) #125

# Multiple variables
multiple_variable = lambda a, b, c: a ** 2 - 3 * b + 4 * c
print(multiple_variable(5, 5, 3)) # 22