#Create a Class
class MyClass:
  x = 25

p1 = MyClass()
print(p1.x)

#The __init__() Method
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Atik", 29)

print(p1.name)
print(p1.age)

#The __str__() Method

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name} {self.age}"

p1 = Person("Atik", 29)

print(p1)

#Create Methods

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()


