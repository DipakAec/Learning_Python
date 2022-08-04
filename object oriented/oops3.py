#Single level inheritance
class Vehicle:
    def __init__(self,price,mileage):
       
        self.price=price
        self.mileage=mileage

    def show_details(self):
       
        print("Price of car is: ",self.price)
        print("Mileage of car is: ",self.mileage)

class Car(Vehicle):
    def __init__(self,price,mileage,tyre,hp):
        super().__init__(price,mileage)
        self.tyre=tyre
        self.hp=hp
    def show_car_details(self):
        print("Number of types are: ", self.tyre)
        print("HP of car",self.hp)

c1=Car(5000000,40,4,400)
c1.show_car_details()