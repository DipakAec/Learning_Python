class Calculator:
    def __init__(self,num):
        self.num=num
    def getSqure(self):
        print(f"Squre of {self.num} is {self.num**2}")

    def getCube(self):
        print(f"Cube of {self.num} is {self.num**3}")

    def getRoot(self):
        print(f"Cube of {self.num} is {self.num**0.5}")

num1=Calculator(25)
num1.getSqure()
num1.getCube()
num1.getRoot()