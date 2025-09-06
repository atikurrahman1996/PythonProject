fruits = ['banana', 'orange', 'mango', 'lemon']                     # list of fruits
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']      # list of vegetables

# Print the lists and it length
print('Lists of Fruits:', fruits)
print('Number of fruits:', len(fruits))
print('Vegetables:', vegetables)
print('Number of vegetables:', len(vegetables))

# Accessing list items using Index

fruits = ['banana', 'orange', 'mango', 'lemon']
first_fruit = fruits[0]
print(first_fruit)      # banana
second_fruit = fruits[1]
print(second_fruit)     # orange

# checking items
fruits = ['banana', 'orange', 'mango', 'lemon']
does_exist = 'banana' in fruits
print(does_exist)  # True
does_exist = 'lime' in fruits
print(does_exist)  # False

# Append (To add item to the end of an existing list we use the method append().

fruits = ['banana', 'orange', 'mango', 'lemon', 'apple']
print(fruits)           # ['banana', 'orange', 'mango', 'lemon', 'apple']
fruits.append('lime')   # ['banana', 'orange', 'mango', 'lemon', 'apple', 'lime]
print(fruits)

# insert
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.insert(2, 'apple') # insert apple between orange and mango
print(fruits)           # ['banana', 'orange', 'apple', 'mango', 'lemon']
fruits.insert(3, 'lime')   # ['banana', 'orange', 'apple', 'mango', 'lime','lemon',]
print(fruits)

# remove
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.remove('banana')
print(fruits)  # ['orange', 'mango', 'lemon']


# pop (The pop() method removes the specified index, (or the last item if index is not specified):

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.pop()
print(fruits)       # ['banana', 'orange', 'mango']

fruits.pop(0)
print(fruits)       # ['orange', 'mango']

# del
fruits = ['banana', 'orange', 'mango', 'lemon']
del fruits[0]
print(fruits)       # ['orange', 'mango', 'lemon']

del fruits[1]
print(fruits)       # ['orange', 'lemon']

# clear
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.clear()
print(fruits)       # []

# copying a lists

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits_copy = fruits.copy()
print(fruits_copy)       # ['banana', 'orange', 'mango', 'lemon']

# join

positive_numbers = [1, 2, 3,4,5]
zero = [0]
negative_numbers = [-5,-4,-3,-2,-1]
integers = negative_numbers + zero + positive_numbers
print(integers)

fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']
fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables )


# count
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.count('orange'))   # 1
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.count(24))           # 3

# Reverse
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.reverse()
print(fruits)

ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.reverse()
print(ages)

# sort
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.sort()
print(fruits)
