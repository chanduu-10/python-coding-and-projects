#Encapsulation means hiding the data inside a class so that no one can change it directly,
#We give access to data only through functions (called getters and setters).


#example 1
"""
class student:
    def __init__(self,name,age):
        self.name = name
        self._age = age #private vairable
    def get_age(self):
        return self._age
    def set_age(self,age):
        if age >0:
            self._age = age
        else:
            print("invalid age!age must be postive")

# Accessing private variable via getter
student1 = student("chandu",22)
print(student1.get_age())  
# Trying to set an invalid age    
student1.set_age(-5)       # Invalid age! Age must be positive.
print(student1.get_age())  
"""

#example 2
"""
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # 🔐 Private variable

    # ✅ Getter - check balance
    def check_balance(self):
        return self.__balance

    # ✅ Setter - deposit money
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"✅ Deposited ₹{amount}")
        else:
            print("❌ Invalid deposit amount")

    # ✅ Setter - withdraw money
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"✅ Withdrawn ₹{amount}")
        else:
            print("❌ Insufficient balance or invalid amount")

# 🎯 Creating an account object
account = BankAccount(1000)  # Opening balance = ₹1000

# ✅ Using getters & setters (like ATM buttons)
print("Current Balance:", account.check_balance())  # ✅ Check balance

account.deposit(500)         # ✅ Deposit ₹500
account.withdraw(300)        # ✅ Withdraw ₹300
account.withdraw(1500)       # ❌ Invalid (Not enough balance)

print("Final Balance:", account.check_balance())

# ❌ Direct access to balance (Not allowed)
# print(account.__balance)   # ❌ Error: balance is private"""

#example 3
#Imagine you have a school bag.
#Your books (data) are inside the bag.
#Only you can open the bag using a zip (method).
#Others can’t directly touch your books
class schoolbag:
    def __init__(self,book1,book2,book3):
        self._books = [book1,book2,book3]
    def open_bag(self):                      
        print("opening bag using zip")   #this is getter->It is used to access (view) the list of books inside the bag.
        return self._books
    def add_book(self,newbook):
        if newbook:
            self._books.append(newbook)
            print(f"added'{newbook}'to the bag")
        else:
            print("invalid book name")   #both add and remove is a setter method —>it is used to add (update) books in the bag (modifies _books list).
    def remove_book(self,book_name):
        if book_name in self._books:
            self._books.remove(book_name)
            print(f"removed'{book_name}'from the bag")
        else:
            print("book not found the bag")
    def search_book(self,book_name):
        if book_name in self._books:
            print(f"Yes,'{book_name}'is in bag")  #search is utility not a getter or setter
        else:
            print(f"No,'{book_name}'is not in the bag") 
    def count_books(self):
        print(f"Total books in the bag:{len(self._books)}")  #count_books() is also more like a getter because it reads the data.


        return len(self._books)
    

my_bag =schoolbag("maths","physics","chemistry")
print("Books in my bag:", my_bag.open_bag())

my_bag.add_book("History")
my_bag.remove_book("maths")
print("Updated bag:",my_bag.open_bag())

my_bag.search_book("physics")
my_bag.search_book("biology")

my_bag.count_books()
        
