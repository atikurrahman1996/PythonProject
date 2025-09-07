#to handle repetitive task programming languages use loops: For...Loop, while...loop

#For...loop

fruits = ["apple", "banana", "cherry"]
for x in fruits:
 print(x)

#For...loop with list
 numbers = [0, 1, 2, 3, 4, 5]
 for number in numbers:
     print(number)

#For...Loop with String
language = 'Python'
for letter in language:
    print(letter)

#For loop with tuple

numbers = (0, 1, 2, 3, 4, 5)
for number in numbers:
    print(number)

#For ...loop with dict
person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}
for key in person:
    print(key)

for key, value in person.items():
    print(key, value)

#Loops in set

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
for company in it_companies:
    print(company)

#Break and Continue

numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        break


numbers = (0, 1, 2, 3, 4, 5)
for number in numbers:
    print(number)
    if number == 3:
        continue
