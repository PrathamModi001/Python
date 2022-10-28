class Train:
    def __init__(self,name,fare,seats):
        self.name = name; self.fare = fare; self.seats = seats
    
    def bookTicket(self):
        if(self.seats>0):
            print(f"Succesfully Booked the seat in the {self.name}. Your seat number is: {self.seats}")
            self.seats = self.seats - 1
        else:
            print(f"Sorry! No seats available at the moment please try in Tatkal.")
    
    def getStatus(self):
        print(f"The number of seats available at the moment are: {self.seats}")
    
    def getFareInfo(self):
        print(f"\nHello Sir,\nThe train you have booked for is the: {self.name} the fare for which is Rs.{self.fare}.")
    
    def cancelTicket(self):
        a = input("Are you sure you want to cancel the ticket ? Press Y or N: ")
        if(a == "Y" or "y"):
            print("Successfully Cancelled the ticket!")
            self.seats = self.seats + 1
        else:
            print("The process of cancelling the ticket is exited.")
    

intercity = Train("Intercity Express",90,2)
intercity.getStatus()
intercity.bookTicket()
intercity.getStatus()
intercity.cancelTicket()
intercity.getFareInfo()
intercity.bookTicket()
intercity.getStatus()
intercity.bookTicket()

