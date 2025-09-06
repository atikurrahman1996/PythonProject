#A tuple is a collection of different data types which is ordered and unchangeable (immutable).
#Tuples are written with round brackets, ()

#Empty tuple: Creating an empty tuple

# syntax
empty_tuple = ()
# or empty_tuple = tuple()

#Creating tuples
fruits = ('banana', 'orange', 'mango', 'lemon')
print(len(fruits)) # find length

#Accessing Tuple Items
first_fruit = fruits[0] #banana
second_fruit = fruits[1] #orange
last_index =len(fruits) - 1  #3
last_fruit = fruits[last_index] #lemon

print(first_fruit)
print(second_fruit)
print(last_index)
print(last_fruit)

#Slicing tuples

fruits = ('banana', 'orange', 'mango', 'lemon')
all_fruits = fruits[0:4]    # all items
#all_fruits= fruits[0:]      # all items
orange_mango = fruits[1:3]  # doesn't include item at index 3
orange_to_the_rest = fruits[1:]

print(all_fruits)
print(orange_mango)
print(orange_to_the_rest)

#Changing Tuples to Lists (We can change tuples to lists and lists to tuples.
# Tuple is immutable if we want to modify a tuple we should change it to a list.

fruits = ('banana', 'orange', 'mango', 'lemon')
fruits = list(fruits)
fruits[0] = 'apple'
print(fruits)     # ['apple', 'orange', 'mango', 'lemon']
fruits = tuple(fruits)
print(fruits)     # ('apple', 'orange', 'mango', 'lemon')

#Checking an Item in a Tuple
fruits = ('banana', 'orange', 'mango', 'lemon')
print('orange' in fruits) # True
print('apple' in fruits) # False

#Joining Tuples

fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage','Onion', 'Carrot')
fruits_and_vegetables = fruits + vegetables

#Deleting Tuples
fruits = ('banana', 'orange', 'mango', 'lemon')
del fruits