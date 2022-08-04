class Train:
    def __init__(self,name,fare,seat):
        self.name=name
        self.fare=fare
        self.seat=seat
    def getInfo(self):
        print(f"Name of train is {self.name} ")
        print(f"Number of seat availeble is {self.seat}")
    
    def getPrice(self):
        print(f"Price of ticket is RS. {self.fare}")

    def bookTicket(self):
        if(self.seat>0):
            print(f"Your seat number is {self.seat}")
            self.seat=self.seat-1
        else:
            print("Sorry! No seat is available,try Tatkal")


t1=Train("Intercity Express",100 ,1)
t1.getInfo()
t1.getPrice()
t1.bookTicket()
t1.bookTicket()
