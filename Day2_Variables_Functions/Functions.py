def my_function():
  print("Hello from a function")

my_function()


def fun():
  print("Welcome to GFG")
fun()

#Arguments

def my_function(fname):
  print(fname +" " "Ariyan")

my_function("AR")
my_function("Atik")
my_function("Ariyan")


def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

#Default Parameter Value (If we call the function without argument, it uses the default value)
def my_function(country = "Bangladesh"):
  print("I am from " + country)

my_function("BD")
my_function()
my_function("UK")

#Passing a List as an Argument

def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)

#own example
def my_calculator(syntactic):
    print("This is a calculator name is: "+ syntactic)

my_calculator("abc")
my_calculator("xyz")
my_calculator("zzz")

#Return Values -> We need to use return statement

def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))
