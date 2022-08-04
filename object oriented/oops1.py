class employee:
    def __init__(self,name,age,salary,gender):
        self.name=name
        self.age=age
        self.salary=salary
        self.gender=gender

    def employee_details(self):
        print("Name of employee is: ",self.name)
        print("Age of employee is: ",self.age)
        print("Salary of employee is: ",self.salary)
        print("Gender of employee is: ",self.gender)

e1=employee('Ram',30,30000,'Male')
e2=employee('Sam',32,35000,'Male')
e1.employee_details()
e2.employee_details()