class Vehicle:
    def __init__(self,name,price,mileage):
        self.name=name
        self.price=price
        self.mileage=mileage

    def show_details(self):
        print("Name of car is: ",self.name)
        print("Price of car is: ",self.price)
        print("Mileage of car is: ",self.mileage)

v1=Vehicle('Tesla',1500000,40)
v2=Vehicle('Tata',1000000,50)
v1.show_details()
v2.show_details()