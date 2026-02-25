#29. Transport Booking

class Transport:
   def book(self):
      pass

class Bus(Transport):
    def book(self):
        print("Bus ticket booked")

class Flight(Transport): 
    def book(self):
        print("Flight ticket booked")

def make_booking(service):
    service.book()

make_booking(Bus())
make_booking(Flight())