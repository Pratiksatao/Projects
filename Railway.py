

trains = []
bookings = []

def add_train():
    train_no = input("Enter Train Number: ")
    total_seats = int(input("Enter Total Seats: "))
    trains.append({'number': train_no, 'seats': total_seats, 'booked_seats': 0})
    print("Train added successfully!")


def seat_ava():
    train_no = input("Enter Train Number: ")
    for train in trains:
        if train['number'] == train_no:
            ava_seat = train['seats'] - train['booked_seats']
            if ava_seat <= 0:
                print("No Seat Available")
            else:
                print("Available seats in Train", train_no, " :- ", ava_seat)
            return
    print("Train not found")

def book():
    train_no = input("Enter Train Number: ")
    ticket_no = int(input("Enter the number of tickets you want: ")) 
        
    for train in trains:
        if train['number'] == train_no:
            ava_seat = train['seats'] - train['booked_seats']
            if ava_seat > 0:
                print("Available seats in Train", train_no, " :- ", ava_seat)
                
                if ticket_no <= ava_seat:
                    for _ in range(ticket_no): 
                        name = input("Enter Passenger Name: ")
                        train['booked_seats'] += 1
                        bookings.append({'train_no': train_no, 'name': name})
                    print("Ticket(s) booked successfully!")
                else:
                    print("Not enough available seats!")
            else:
                print("No Seat Available")
            return
    print("Train not found")

def cancel_t():
    p_name = input("Enter Passenger Name for ticket cancellation: ")
    for booking in bookings:
        if booking['name'] == p_name:
            for train in trains:
                if train['number'] == booking['train_no']:
                    train['booked_seats'] -= 1
                    bookings.remove(booking)
                    print("Ticket cancelled successfully!")
                    return
    print("Booking not found!")

def display_tickets():
    if bookings:
        print("Ticket Details:")
        for booking in bookings:
            print(f"Train No: {booking['train_no']}, Passenger Name: {booking['name']}")
    else:
        print("No bookings found.")

print("==============================================================")
print("WELCOME TO RAILWAY RESERVATION SYSTEM")
while True:
    print("==============================================================")
    print("1. Add Train\n2. Check Seat Availability\n3. Book Ticket\n4. Cancel Ticket\n5. Display Tickets Details\n6. Exit")
    print("==============================================================")
    choice = int(input("Enter Your Choice :- "))
    if choice == 1:
        add_train()
    elif choice == 2:
        seat_ava()
    elif choice == 3:
        book()    
    elif choice == 4:
        cancel_t()
    elif choice == 5:
        display_tickets()
    elif choice == 6:
        print("Thank you for your time. Please visit again!")
        break
    else:
        print("Invalid choice! Please try again.")

