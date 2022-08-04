class Person:
    country="India"
    def takeBreath(self):
        print("I am Breathing...")

class Employee(Person):
    company="TCS"
    def getSalary(self):
        print(f"Salary is {self.salary}")

    def takeBreath(self):
        print("I am Employee I am also Breathing...")

class Programmer(Employee):
    def getSalary(self):
        print("No Salary for this month.")
    
    def takeBreath(self):
        print("I am programmer I am  Breathing++")

pe=Person()
em=Employee()
pr=Programmer()

pr.getSalary()
pr.takeBreath()
pr.takeBreath()
print(Person.country)