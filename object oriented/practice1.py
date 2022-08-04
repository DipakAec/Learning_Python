class Programmer:
    company="microsoft"
    def __init__(self,name,product):
        self.name=name
        self.product=product
    def getInfo(self):
        print(f"Name of the {self.company} programmer is {self.name} and product he is working on is {self.product}")
ram=Programmer('Ram','GitHub')
sam=Programmer('Sam','VS Code')

ram.getInfo()
sam.getInfo()

