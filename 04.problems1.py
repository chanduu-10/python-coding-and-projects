"""class programmer:

    def __init__(self,name,salary,company):
        self.name = name
        self.salary = salary
        self.company = company

staff0=programmer ("chandu",71000,"microsoft")
staff1=programmer ("pandu",91000,"microsoft")
staff2=programmer ("gopi",71000,"microsoft")
print(staff0.name,staff0.salary,staff0.company)
print(staff1.name,staff1.salary,staff1.company)
print(staff2.name,staff2.salary,staff2.company)"""

"""class number:

    def __init__(self,num):              
        self.num = num

square = number(5)
print(square.num * square.num)           
cube = number(5)
print(cube.num * cube.num * cube.num)
squareroot = number(1000)
print(squareroot.num ** 0.5)"""

"""class chandu:               
    a = 0

shannu = chandu()
#print(shannu.a)               
shannu.a = 1
print(shannu.a)"""

"""
class number:

    def __init__(self,num):             #class attributes
        self.num = num

    @staticmethod
    def shannu():
            print("hey this is number and i've print square and cube,squarerrot")

    
square = number(5)                      #object attributes
print(square.num * square.num)
cube = number(5)                            
print(cube.num * cube.num * cube.num)
squareroot = number(1000)
print(squareroot.num ** 0.5)
square.shannu() """

from random import randint
class train:

    def __init__(self,trainno):
        self.trainno = trainno

    def book(self,fro,to):
        print(f"train is booked from {fro} to {to}")

    def status(self,fro,to):
        print(f"{self.trainno} is currtely from {fro} to {to}")

    def conformstatus(self,fro,to):
        print(f"{self.trainno}is conform from {fro} to {to} and cost is {randint(699,1999)}")

railways = train(12656)
railways.book("hyderbad","banglore")
railways.conformstatus("hyderabad","banglore")






    