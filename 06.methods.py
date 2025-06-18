#super method in function
"""
class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):
        super().sound()
        print("Dog barks")

d = Dog()
d.sound() """

#super method using __init__constructor
"""
class Animal:
    def __init__(self, species):
        self.species = species
        print(f"Animal is a {self.species}")

class Dog(Animal):
    def __init__(self, breed):
        # Call the constructor of Animal class
        super().__init__("dog")
        self.breed = breed
        print(f"Breed is {self.breed}")

# Creating an object of Dog

d = Dog("german")"""

#super method 
"""class Animal:
    def __init__(self):
      
        print(f"Animal is a dog")

class Dog(Animal):
    def __init__(self):
        # Call the constructor of Animal class
        super().__init__()
        print(f"Breed is german")

d = Dog()"""

#super method
"""
class srinu:
    def __init__(self):
        print("constructor of srinu")
    a = 1

class renu(srinu):
    def __init__(self):
        super().__init__()
        print("constructor of renu")
    b = 2

class chandu(renu):
    def __init__(self):
        super().__init__()
        print("constructor of chandu")
    c = 3

person = chandu()
print(person.c)"""

#class method
"""
class srinu:
    a=1
    @classmethod
    def show(cls):
        print(f"the class attribute of a is {cls.a} ")
    def __str__(cls):
        return f"{cls.a}"
e = srinu()
print(e)
"""
#class method 
"""
class srinu:
    a=1
    def __init__(self,a):
        self.a=a

    @classmethod 
    def __str__(cls):        #srting method 
        return f"{self.a}" 


e = srinu(5)

print(e)
"""
# opeaorts
"""
class a:
    def __init__(self,n):
        self.n=n
    def __floordiv__(self,m):
        return self.n//m.n
    def __mul__(self,m):
        return self.n*m.n
e=a(5)
b=a(5)
print(e//b)
print(e*b)
"""
# length
"""class MyList:
    def __init__(self,items):
        self.items=items
    def __len__(self):
        return len(self.items)
e=  MyList([1,2,3,8])
print(len(e)) """

#@property
# @property is a built-in Python decorator used in Object-Oriented Programming to turn a method into a read-only attribute.
# It allows you to access the method without using parentheses, as if it were a normal variable.
# The @ symbol in Python is used to apply a decorator to a function or method
# A decorator is a function that modifies the behavior of another function.
"""
class srinu:
    def __init__(self,radius):
        self.radius = radius  #radius is an attribute
    @property
    def area(self):
        return 3.14 *(self.radius ** 2)
c = srinu(5)
print(c.area)
"""
"""
class Person:
   
    def __init__(self, age):
        self.age = age
    @property
    def name(self):
        return self.pname
    @name.setter
    def name(self,value):
        self.pname=value


p = Person(25)
p.name="chandu"
print(p.name)  # Accessing like an attribute, but it's a method inside
"""
class employee:
      
    increment=20
    
    @property
    def incre_salary(self):
        return self.esalary
    @incre_salary.setter
    def incre_salary(self,value):
        incre_salary=(self.salary+value)
e=employee()
e.salary=50000
incre_salary=50
print(incre_salary+e.salary)