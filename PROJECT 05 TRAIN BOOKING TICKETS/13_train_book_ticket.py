class Train:
    def __init__(self,name,seats,fare):

     self.name = name 
     self.seats = seats
     self.fare = fare
    def getStatus(self):
       print("***********")
       print(f"The number of train is {self.name}")
       print(f"The seats available in the train are {self.seats}")
       print("***********")

    def getfareInfo(self):
       print(f"The price of the ticket is: Rs.{self.fare}")
    def bookTicket(self):   
       if(self.seats>0):
         print(f"Your ticket has been booked! your seat number is {self.seats}")  
         self.seats = self.seats - 1
       else:
          print(f"Sorry this train is full! kindly try later")
    def cancelTicket(self,seatNo):
       pass    

nonstop = Train( "nonstop: 1133 ", 2, 20)    
nonstop.getStatus()
nonstop.bookTicket()
nonstop.bookTicket()
nonstop.bookTicket()
nonstop.getStatus()
