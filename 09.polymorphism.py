#polymorphism
"""Polymorphism" means — same thing behaving differently.

🔁 In Python, the same function or method can act differently depending on the object or data type it is used with.

Just like:

A boy says "Hello" to his teacher politely 👨‍🏫

Same boy says "Hello" to his friend casually 😎

👉 Same word = "Hello", but behaves differently based on the person.

That is called Polymorphism in OOP!"""


#ex-1
"""
class Vehicle:
    def start(self):
        print("Starting vehicle...")

class Car(Vehicle):
    def start(self):
        print("Starting car...")    

class Bike(Vehicle):
    def start(self):
        print("Starting bike...")
        
for v in [Car(),Bike()]:
    v.start()"""
#ex-2
"""
print(len("ApnaCollege"))     # 12 → length of string
print(len([1, 2, 3]))         # 3 → length of list
print(len({"a": 1, "b": 2}))"""  # 2 → length of dictionary
#One function len() → works on string, list, dictionary.
#That is Polymorphism.
#ex-3
"""
class Cat:
    def speak(self):
        print("Meow")

class Dog:
    def speak(self):
        print("Woof")

# Using both classes
cat1 = Cat()
dog1 = Dog()

cat1.speak()  # Meow
dog1.speak()  # Woof
Both classes have a method called speak(), but it behaves differently. That is Polymorphism
"""
#ex-4
class Laptop:
    def code(self):
        print("Coding on laptop")

class Mobile:
    def code(self):
        print("Coding on mobile")

def developer(device):
    device.code()

developer(Laptop())  # Coding on laptop
developer(Mobile())  # Coding on mobile
#Same function developer() is working with different classes — because both have a code() method.



