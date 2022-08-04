#Single level inheritance
class Employee:
    company="Google"

    def showDetails(self):
        print("This is inside Employee Class")

class programmer(Employee):
    language="python"

    def getLang(self):
        print(f"The language of programmer is: {self.language}")

    def showDetails(self):
        print("This is inside programmer Class")

e=Employee()
p=programmer()
p.showDetails()
p.getLang()