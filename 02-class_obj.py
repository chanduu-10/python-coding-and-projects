class chandu:
    language = "python"             #class attributes
    salary = 71000

    def job(self):                  #self aruguments function
        print(f"language is {self.language} and salary is {self.salary}")

    @staticmethod
    def work():                     #Here we didnot use self aruguments
        print(f"iam working right now banglore with company  soligenix")


employee = chandu()
employee.salary = 72000                 #(object)instance attributes
employee.company = "solugenix"
print(employee.company)
print(employee.language)
print(employee.salary)
employee.job()
employee.work()