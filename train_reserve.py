class Train:
    def __init__(self, name, classes):
        self.name = name
        self.classes = classes  # Dictionary to store available seats in different classes

    def check_availability(self, coach):
        if coach in self.classes:
            return self.classes[coach] > 0
        return False

    def book_ticket(self, coach, num_tickets):
        if self.check_availability(coach):
            if self.classes[coach] >= num_tickets:
                self.classes[coach] -= num_tickets
                return True
            else:
                return False
        return False

def display_trains(trains):
    print("Available trains and their classes:")
    for index, train in enumerate(trains):
        print(f"{index + 1}. {train.name}")
        for coach, seats in train.classes.items():
            print(f"   {coach}: {seats} seat(s) available")
        if all(seats == 0 for seats in train.classes.values()):
            print("   Fully Booked")

def main():
    # Create train instances
    trains = [
        Train('Rajdhani', {'Sleeper': 3, 'First AC': 9, 'Third AC': 11}),
        Train('Shatabdi', {'First Class': 13, 'Third AC': 1, 'Second AC': 6, 'Sleeper': 3}),
        Train('Vandebharat', {'All Classes': 0}),
        Train('Ajanta', {'All Classes': 0}),
        Train('Gautami', {'All Classes': 0})
    ]

    while True:
        display_trains(trains)
        try:
            choice = int(input("Enter the number of the train you want to book (1-5) or 0 to exit: "))
            if choice == 0:
                print("Exiting...")
                break

            if 1 <= choice <= 5:
                train = trains[choice - 1]
                if any(train.check_availability(coach) for coach in train.classes):
                    print("Available classes:")
                    for coach in train.classes:
                        if train.check_availability(coach):
                            print(f"   {coach}: {train.classes[coach]} seat(s) available")
                    
                    coach = input("Enter the class you want to book (e.g., 'Sleeper', 'First AC', 'Third AC', etc.): ")
                    if train.check_availability(coach):
                        try:
                            num_tickets = int(input("Enter the number of tickets to book: "))
                            if num_tickets > 0 and train.book_ticket(coach, num_tickets):
                                print(f"Successfully booked {num_tickets} ticket(s) in {coach} on {train.name}.")
                            else:
                                print("Failed to book tickets. Either not enough seats available or invalid number of tickets.")
                        except ValueError:
                            print("Invalid input. Please enter a valid number of tickets.")
                    else:
                        print(f"Sorry, no seats available in {coach} class on {train.name}.")
                else:
                    print(f"Sorry, {train.name} is fully booked.")
            else:
                print("Invalid choice. Please select a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a valid train number.")

if __name__ == "__main__":
    main()
