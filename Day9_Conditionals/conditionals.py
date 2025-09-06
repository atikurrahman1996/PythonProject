#If Condition
a = 3
if a > 0:
    print('A is a positive number')
# A is a positive number

#If Else (If condition is true the first block will be executed, if not the else condition will run.)

a = 3
if a < 0:
    print('A is a negative number')
else:
    print('A is a positive number')

#If Elif Else (We use elif when we have multiple conditions.)
a = 10
if a > 20:
    print('A is a positive number')
elif a < 10:
    print('A is a negative number')
else:
    print('A is: 10')

#Nested Conditions

a = 0
if a > 0:
    if a % 2 == 0:
        print('A is a positive and even integer')
    else:
        print('A is a positive number')
elif a == 0:
    print('A is zero')
else:
    print('A is a negative number')

#excercise: Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback:
# You are old enough to drive. If below 18 give feedback to wait for the missing amount of years

age = int(input("Enter your age: "))

if age >= 18:
    print("You are old enough to drive.")
else:
    years_left = 18 - age
    print(f"You need to wait {years_left} more year(s) to start driving.")
