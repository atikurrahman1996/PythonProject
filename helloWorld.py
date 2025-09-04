print("hello world, this is my first program")

#Indentation
if 5 > 2:
 print("Five is greater than two!")


 #DataType
'''
str: "hello world"
int: 10
float: x =20.5
complex: x = 1j
list : x = ["apple", "banana", "cherry"]
tuple :x = ("apple", "banana", "cherry")
range :
dict : x = {"name" : "John", "age" : 36}
set :x = {"apple", "banana", "cherry"}
frozenset :x = frozenset({"apple", "banana", "cherry"})
bool: True/false
bytes, bytearray, memoryview

'''

#Finding DataType
 x = 5
 print(type(x))

#Finding length
 a = "Hello, World!"
 print(len(a))

 '''
 Python Collections (Arrays):
There are four collection data types in the Python programming language:

List- is a collection which is ordered and changeable. Allows duplicate members.
Tuple- is a collection which is ordered and unchangeable. Allows duplicate members.
Set- is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary- is a collection which is ordered** and changeable. No duplicate members.
 '''

 #list (Lists are one of 4 built-in data types others 3 are Tuple, Set, and Dictionary),

 mylist = ["apple", "banana", "cherry"]
 print(mylist)

#List allow duplicates
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

#Tuple
mytuple = ("apple", "banana", "cherry")
print(mytuple)

#Set

myset = {"apple", "banana", "cherry"}
print(myset)

#Dictionary

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)