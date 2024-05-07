class Vehicle:
    def __init__(self, name):
        self.name = name

    def fare(self, capacity, distance):
        base_fare = capacity * distance * 2.15
        return base_fare


class Bus(Vehicle):
    def __init__(self, name, capacity):
        super().__init__(name)
        self.capacity = capacity

    def fare(self, distance):
        base_fare = super().fare(self.capacity, distance)
        maintenance_charge = base_fare * 0.1
        total_fare = base_fare + maintenance_charge
        return total_fare


def main():
    while True:
        bus_name = input("Enter Bus Name: ")
        capacity = int(input("Enter Capacity: "))
        distance = int(input("Enter Distance: "))

        if capacity <= 0 or distance <= 0:
            print("Invalid input. Capacity and distance must be positive.")
            continue

        bus = Bus(bus_name, capacity)

        total_fare = bus.fare(distance)

        print("\nBus Details:")
        print(f"Bus Name: {bus.name}")
        print(f"Total Seat: {bus.capacity}")
        print(f"Traveled Distance: {distance}")
        print(f"Total Fare: {total_fare:.2f} Taka")

        choice = input("\nDo you want to calculate another fare (y/n)? ")
        if choice.lower() != 'y':
            break


if __name__ == "__main__":
    main()
