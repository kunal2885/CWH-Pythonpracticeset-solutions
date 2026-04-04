no_of_seats = 10
class Train:
    passenger_name = ""
    def __init__(slf,name):
        slf.passenger_name= name
    
    def book_ticket(slf):
        global no_of_seats
        if(no_of_seats < 1):
            print("no more seats left!!!")
            return
        print("booking the ticket...")
        print(f"Congrats! {slf.passenger_name} your ticket has been booked")
        
        no_of_seats= no_of_seats-1
    def get_status(slf):
        print(f"number of seats left are : {no_of_seats}")
    def get_fare_info(slf):
        print(f"total fare charges are {len(slf.passenger_name)*100}")

kunal = Train("kunal")
kushal = Train("kushal")
kunal.book_ticket()
kunal.get_status()
kunal.get_fare_info()