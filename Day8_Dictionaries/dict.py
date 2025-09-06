#A dictionary is a collection of unordered, modifiable(mutable) paired (key: value) data type.

#empty_dict
empty_dict = {}
print(empty_dict)

#Creating a Dictionary
person = {
    'first_name':'ATIK',
    'last_name':'ARIYAN',
    'age':299,
    'country':'BD',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Dhanmondi',
        'city': 'Dhaka',
        'zipcode':'02210'
    }
    }
print(person)
print(len(person)) # 7

#Accessing Dictionary Items

print(person['first_name']) # ATIK
print(person['country'])    # DB
print(person['skills'])     # ['JavaScript', 'React', 'Node', 'MongoDB', 'Python']
print(person['skills'][0])  # JavaScript
print(person['address']['street'])
print(person['address']['city'])

#Adding Items to a Dictionary

person['job_title'] = 'Instructor'
person['skills'].append('HTML')
print(person)
print(len(person)) # 8

#Modifying Items in a Dictionary
person['first_name'] = 'AR KHAN'
person['age'] = 25
print(person)

#Removing Key and Value Pairs from a Dictionary
#pop(key): removes the item with the specified key name:
#popitem(): removes the last item
#del: removes an item with specified key name

person.pop('first_name')        # Removes the firstname item
person.popitem()                # Removes the address item
del person['is_marred']
print(person)