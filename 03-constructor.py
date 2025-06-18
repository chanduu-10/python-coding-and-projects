class chandu:
    language = "python"             #class attributes
    salary = 71000

    def job(self):                  #self aruguments function
        print(f"language is {self.language} and salary is {self.salary}")

    @staticmethod
    def work():                     #Here we didnot use self aruguments
        print(f"iam working right now banglore with company name soligenix")

    def __init__(self):
        print("this is first constructor")#when ever u creates constructor its print start of code,object calls first __init__ constructor only
                                    #The __init__ constructor in Python is a special method used when creating (initializing) objects from a class. 
                                    # It’s automatically called when a new object is created.
    def __init__(self,name,salary):
        self.name=name
        self.salary = salary
        print("this is second constructor")


employee = chandu("chandu",80000)
print(employee.name,employee.salary)
employee.salary = 72000                 #(object)instance attributes
print(employee.language)
employee.job()
employee.work()