'''
Python Variable Name Rules

A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (firstname, Firstname, FirstName and FIRSTNAME) are different variables)
'''


# Variables in Python

first_name = 'Atikur'
last_name = 'Rahman'
country = 'BD'
city = 'DHAKA'
age = 29
is_married = False
skills = ['HTML', 'CSS', 'JS', 'React', 'Python']
person_info = {
    'firstname':'Atikur',
    'lastname':'Rahman',
    'country':'BD',
    'city':'Dhaka'
    }

# Printing the values stored in the variables

print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)
print('Skills: ', skills)
print('Person information: ', person_info)


# Declaring multiple variables in one line

first_name, last_name, country, age, is_married = 'Atik', 'Ariyan', 'Dhaka', 29, False

print(first_name, last_name, country, age, is_married)
print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)
print('Married: ', is_married)