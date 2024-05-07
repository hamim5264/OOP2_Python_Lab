class Fare_Calc:
    def __init__(self, bus_name, passenger_name):
        self.fare = None
        self.bus_name = bus_name
        self.passenger_name = passenger_name
        self.distance = 0.0

    def set_distance(self, distance):
        if distance > 0:
            self.distance = distance
        else:
            print(f"Invalid distance for {self.passenger_name}. Please enter a positive value.")

    def calculate_fare(self):
        self.fare = self.distance * 2.15

    def display_info(self):
        print(f"\nPassenger Information")
        print(f"Bus Name: {self.bus_name}")
        print(f"Passenger Name: {self.passenger_name}")
        print(f"Traveled Distance: {self.distance:.1f} km")
        print(f"Fare is: {self.fare:.2f} Taka")


def main():
    num_passengers = int(input("How many passengers: "))

    passengers = []
    for i in range(num_passengers):
        bus_name = input(f"\nEnter bus Name for passenger {i + 1}: ")
        passenger_name = input(f"Enter passenger Name: ")
        passenger = Fare_Calc(bus_name, passenger_name)

        distance = float(input(f"Distance for {passenger_name}: "))
        passenger.set_distance(distance)

        passengers.append(passenger)

    for passenger in passengers:
        passenger.calculate_fare()
        passenger.display_info()


if __name__ == "__main__":
    main()
