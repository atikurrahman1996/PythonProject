#Syntext
'''
try:
    code in this block if things go well
except:
    code in this block run if things go wrong
'''

#Example:

try:
    name = input('Enter your name:')
    year_born = input('Year you were born:')
    age = 2025 - year_born
    print(f'You are {name}. And your age is {age}.')
except:
    print('Something went wrong')

#In the above example, the exception block will run and we do not know exactly the problem.

#In the following example, it will handle the error and will also tell us the kind of error raised.

try:
    name = input('Enter your name:')
    year_born = input('Year you were born:')
    age = 2025 - year_born
    print(f'You are {name}. And your age is {age}.')
except TypeError:
    print('Type error occured')  # Output: Type Error
except ValueError:
    print('Value error occured')
except ZeroDivisionError:
    print('zero division error occured')

#In the code above the output is going to be TypeError. Now, let's add an additional block:


try:
    name = input('Enter your name:')
    year_born = input('Year you born:')
    age = 2025 - int(year_born)
    print(f'You are {name}. And your age is {age}.')
except TypeError:
    print('Type error occur')
except ValueError:
    print('Value error occur')
except ZeroDivisionError:
    print('zero division error occur')
else:
    print('I usually run with the try block')
finally:
    print('I alway run.')

#It is also shorten the above code as follows:

try:
    name = input('Enter your name:')
    year_born = input('Year you born:')
    age = 2019 - int(year_born)
    print(f'You are {name}. And your age is {age}.')
except Exception as e:
    print(e)


#Spreading in Python

lst_one = [1, 2, 3]
lst_two = [4, 5, 6, 7]
lst = [0, *lst_one, *lst_two]
print(lst)          # [0, 1, 2, 3, 4, 5, 6, 7]

country_lst_one = ['Finland', 'Sweden', 'Norway']
country_lst_two = ['Denmark', 'Iceland']
nordic_countries = [*country_lst_one, *country_lst_two]
print(nordic_countries)  # ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']