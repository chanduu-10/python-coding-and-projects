#abstraction means hiding the complex internal details and showing only the necessary features of an object.
#steps
#1. Import ABC module
#2. Create an Abstract Class
#3. Create Subclasses that implement the abstract method
#4. Using the subclasses
"""
from abc import ABC, abstractmethod
class Animal(ABC):  # ABC makes it an abstract class
    @abstractmethod
    def make_sound(self):
        pass
class Dog(Animal):
    def make_sound(self):
        return "Bark"

class Cat(Animal):
    def make_sound(self):
        return "Meow"
d = Dog()
print(d.make_sound())  # Output: Bark

c = Cat()
print(c.make_sound())"""  # Output: Meow
#a = Animal()You'll get an error: ❌ TypeError: Can't instantiate abstract class Animal with abstract method make_sound
#That’s abstraction — you’re forced to create a specific type of object (like Dog or Cat), not a generic one like Animal.

from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCardPayment(PaymentProcessor):
    def pay(self, amount):
        print(f"Paid {amount} using Credit Card.")

class PayPalPayment(PaymentProcessor):
    def pay(self, amount):
        print(f"Paid {amount} using PayPal.")

payment = CreditCardPayment()
payment.pay(500)  # Paid 500 using Credit Card

payment2 = PayPalPayment()
payment2.pay(200)  # Paid 200 using PayPal
