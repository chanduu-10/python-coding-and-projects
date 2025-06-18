"""class twoD:
    def __init__(self,i,j):
        self.i = i
        self.j = j
    def show(self):
        print(f"twodimension is: {self.i}i +{self.j}j")

class threeD(twoD):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.k = k
    def show(self):
        print(f"threedimension is :{self.i}i +{self.j}j + {self.k}k")
    
supervector = twoD(1,2)
supervector.show()
supervector = threeD(1,2,3)
supervector.show()"""

"""
import random
actualnumber = random.randint(1,3)
num = int(input("enter a player number:"))
if num > actualnumber:
    print(f"sorry this is not perfect guess,it is lower than actual number:")
elif num < actualnumber:
    print(f"sorry this is not perfect guess,it is higher is than num ")
else:
    print(f'your are right,this is perfect guess')"""

import random
actualnumber = random.randint(1,3)
num=int(input("enter your number:"))
while (num != actualnumber):
    if num > actualnumber:
       print(f"sorry this is not perfect guess,it is lower than actual number:")
    else:
       print(f'your are right,this is perfect guess')
    num=int(input("enter your number"))

print("you are correct!,this is perfect guess")


