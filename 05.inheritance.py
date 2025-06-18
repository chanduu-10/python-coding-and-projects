#single inheritance 
"""class srinu:
    def properties(self,money):
        print(f"money is {money}")

class renu(srinu):
    a = "drinker"
    def job(self,profession):
        print(f"profession is {profession}")


employee = renu()
employee.properties(7000000)
employee.job("teacher")
print(employee.a) """

#hirerachial inheritance
"""
class srinu:
    def properties(self,money):
        print(f"money is {money}")
class renu(srinu):
    def habits(self,qualites):
        print(f"qualites is {qualites}")
class chandu(srinu):
    def skills(self,skills):
        print(f"skills is {skills}")

person1 = renu()
person2 = chandu()
person1.properties(7000000)
person1.habits("good")
person2.properties(7000000)
person2.skills("coding")"""
 
#multiple inheritance
"""class srinu:
    def properties(self,money):
        print(f"money is {money}")
class durga:
    def quality(self,qualites):
        print(f"quality is {qualites}")

class chandu(srinu,durga):
    a = "nobadhabits"
    def job(self,salary):
        print(f"salary is {salary}")

person = chandu()
person.properties(5500000)
person.quality("hardworker")
person.job(750000)
print(person.a)"""

#multilevel inheitance
"""class srinu:
    def properties(self,money):
        print(f"money is {money}")
class renu(srinu):
    def habits(self,qualites):
        print(f"qualites is {qualites}")

class chandu(renu):
    def skills(self,skills):
        print(f"skills is {skills}")

person = chandu()
person.properties(446554)
person.habits("good")
person.skills("coding")"""

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
d.sound()

"""
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


class Animal:
    def __init__(self):
      
        print(f"Animal is a dog")

class Dog(Animal):
    def __init__(self):
        # Call the constructor of Animal class
        super().__init__()
        print(f"Breed is german")

d = Dog()

