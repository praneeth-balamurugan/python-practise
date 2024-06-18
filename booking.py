class Flight:
    id = 0

    def __init__(self):
        Flight.id += 1
        self.flightID = Flight.id
        self.tickets = 50
        self.price = 5000
        self.passengerDetails = []
        self.passengerIDs = []
        self.bookedTicketsPerPassenger = []
        self.passengerCost = []

    def add_passenger_details(self, passenger_detail, number_of_tickets, passenger_id):
        self.passengerDetails.append(passenger_detail)
        self.passengerIDs.append(passenger_id)
        self.passengerCost.append(self.price * number_of_tickets)

        self.price += 200 * number_of_tickets
        self.tickets -= number_of_tickets
        self.bookedTicketsPerPassenger.append(number_of_tickets)
        print("Booked Successfully!")

    def cancel_ticket(self, passenger_id):
        if passenger_id not in self.passengerIDs:
            print("Passenger ID not found!")
            return

        index_to_remove = self.passengerIDs.index(passenger_id)
        tickets_to_cancel = self.bookedTicketsPerPassenger[index_to_remove]

        self.tickets += tickets_to_cancel
        self.price -= 200 * tickets_to_cancel

        print("Refund Amount after cancel:", self.passengerCost[index_to_remove])

        del self.bookedTicketsPerPassenger[index_to_remove]
        del self.passengerIDs[index_to_remove]
        del self.passengerDetails[index_to_remove]
        del self.passengerCost[index_to_remove]

        print("Cancelled Booked Tickets Successfully!")

    def flight_summary(self):
        print("Flight ID", self.flightID, "-- Remaining Tickets", self.tickets, "-- Current Ticket Price", self.price)

    def print_details(self):
        print("Flight ID", self.flightID, "->")
        for detail in self.passengerDetails:
            print(detail)


def book(current_flight, tickets, passenger_id):
    passenger_detail = f"Passenger ID {passenger_id} -- Number of Tickets Booked {tickets} -- Total cost {current_flight.price * tickets}"
    current_flight.add_passenger_details(passenger_detail, tickets, passenger_id)

    current_flight.flight_summary()
    current_flight.print_details()


def cancel(current_flight, passenger_id):
    current_flight.cancel_ticket(passenger_id)
    current_flight.flight_summary()
    current_flight.print_details()


def main():
    flights = [Flight() for _ in range(2)]
    passenger_id = 1

    while True:
        print("1. Book 2. Cancel 3. Print")
        choice = int(input())

        if choice == 1:
            print("Enter Flight ID")
            fid = int(input())

            if fid > len(flights):
                print("Invalid flight ID")
                continue

            current_flight = next((f for f in flights if f.flightID == fid), None)
            if not current_flight:
                continue

            current_flight.flight_summary()

            print("Enter number of tickets")
            t = int(input())

            if t > current_flight.tickets:
                print("Not Enough Tickets")
                continue

            book(current_flight, t, passenger_id)
            passenger_id += 1

        elif choice == 2:
            print("Enter flight ID and passenger ID to cancel booking")
            fid = int(input())

            if fid > len(flights):
                print("Invalid flight ID")
                continue

            current_flight = next((f for f in flights if f.flightID == fid), None)
            if not current_flight:
                continue

            pid = int(input())
            cancel(current_flight, pid)

        elif choice == 3:
            for f in flights:
                if not f.passengerDetails:
                    print("No passenger Details for Flight", f.flightID)
                else:
                    f.print_details()

        else:
            break


if __name__ == "__main__":
    main()
