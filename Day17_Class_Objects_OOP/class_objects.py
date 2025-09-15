#Class constructor

class Person:
    def __init__(self, firstname, lastname, age, country, city):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.city = city


p = Person('Atikur', 'Rahman', 25, 'Bangladesh', 'DHAKA')
print(p.firstname)
print(p.lastname)
print(p.age)
print(p.country)
print(p.city)


#Object Methods
class Person:
    def __init__(self, firstname, lastname, age, country, city):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.city = city

    def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}'


p = Person('Atik', 'Ariyan', 25, 'Bangladesh', 'Dhaka')
print(p.person_info())