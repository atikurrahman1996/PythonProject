#Set is a collection of unordered and un-indexed distinct elements.
#Creating a Set
fruits = {'banana', 'orange', 'mango', 'lemon'}
print(len(fruits))

#Checking an Item
fruits = {'banana', 'orange', 'mango', 'lemon'}
print('mango' in fruits ) # True

#Access specific item
for fruit in fruits:
    if fruit == "mango":
        print("The fruit name is:", fruit)


#adding item
fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.add('lime')
print(fruits)

#Add multiple items using update() The update() allows to add multiple items to a set.
fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = ('tomato', 'potato', 'cabbage','onion', 'carrot')
fruits.update(vegetables)
print(fruits)

#Removing Items from a Set using Pop()

fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.pop()  # removes a random item from the set
print(fruits)

#Clearing Items in a Set

fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.clear()
print(fruits) # set()

#delete set
fruits = {'banana', 'orange', 'mango', 'lemon'}
del fruits

#Converting List to Set
fruits = ['banana', 'orange', 'mango', 'lemon','orange', 'banana']
fruits = set(fruits) # {'mango', 'lemon', 'banana', 'orange'}
print(fruits)

#Joining Sets

fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage','onion', 'carrot'}
print(fruits.union(vegetables)) # {'lemon', 'carrot', 'tomato', 'banana', 'mango', 'orange', 'cabbage', 'potato', 'onion'}

