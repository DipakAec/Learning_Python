class Employee:
    company="google"    #CLASS ATRIBUTES

ram=Employee()
sam=Employee()
ram.salry=15000     #intance atributes
sam.salry=20000     #intance atributes
Employee.company="Youtube" #Changing class atributes
print(ram.company)
print(sam.company)
print(ram.salry)
print(sam.salry)
