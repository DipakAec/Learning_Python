#Multiple Inheritance
class Employee:
    company="Visa"
    eCode=205

class Freelancer:
    company="Microsoft"
    level=0

    def upgradeLevel(self):
        self.level=self.level+1

class Programmer(Employee,Freelancer):
    name="Ram"

p=Programmer()
p.upgradeLevel()
print(p.company)
print(p.eCode)
print(p.level)
