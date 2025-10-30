from classroom import BookingSystem, START_HOUR, END_HOUR

# File used to save and load all room and booking data
FILENAME = "bookings_final_state.csv"

if __name__ == "__main__":
    print("Welcome to the Classroom Booking System!")
    print("-" * len("Welcome to the Classroom Booking System!"))

    # Create a booking system object
    system = BookingSystem()
    print(f"(System loads data from {FILENAME}...)")
    system.load_data(FILENAME)
    print(f"Rooms loaded successfully!")

    # Menu loop for user choices
    while True:
        print("\nWhat would you like to do?")
        print("1. Create a new Room")
        print("2. Find Available Rooms")
        print("3. Book a Room")
        print("4. View a Room's Schedule")
        print("5. Exit")
        option = input("Enter your choice: ").strip()
        print()

        if option == "1":
            # Adding a new room to the system
            print("--- Create a New Room ---")
            room_no = input("Enter Room No. (e.g., NAB101): ").strip()
            building = input("Enter Building Name: ").strip()
            capacity = int(input("Enter Capacity: ").strip())
            try:
                system.create_room(room_no, building, capacity)
            except Exception as e:
                print(e)
                continue
            system.save_data(FILENAME)
            print(f"Success: Room with number as '{room_no}' has been created!")

        elif option == "2":
            # Searching for available rooms based on filters
            building_filter = set(system.rooms.values())
            capacity_filter = set(system.rooms.values())
            hour_filter = set(system.rooms.values())

            print("--- Find Available Rooms ---")
            building = input("Enter the Building Name (Default=None): ").strip()
            capacity = input("Enter Minimum Capacity (Default=0): ").strip()
            hour = input(f"Enter the free hour [{START_HOUR}-{END_HOUR}] (Default=None): ").strip()
            
            if building:
                building_filter = system.filter_by_building(building)
            if capacity:
                capacity_filter = system.filter_by_capacity(int(capacity))
            if hour:
                hour = int(hour)
                if not (START_HOUR <= hour <= END_HOUR):
                    print(f"Please enter a valid hour ({START_HOUR}-{END_HOUR})!")
                hour_filter = system.filter_by_hour(hour)
            
            # Combine all filters using intersection
            final_filter = list(building_filter.intersection(capacity_filter).intersection(hour_filter))
            if not final_filter:
                print("No such rooms found!")
                continue

            for room in final_filter:
                print(f"ID: {room.room_no}, Building: {room.building}, Capacity: {room.capacity}")

        elif option == "3":
            # Booking a room for a particular hour
            print("--- Book a Room ---")
            room_no = input("Enter Room ID to book: ").strip()
            hour = int(input(f"Enter hour to book ({START_HOUR}-{END_HOUR}): ").strip())
            try:
                system.book_room(room_no, hour)
            except Exception as e:
                print(e)
                continue
            system.save_data(FILENAME)
            print(f"Success: Room '{room_no}' booked for hour '{hour}'!")

        elif option == "4":
            # Viewing schedule of a specific room
            print("--- View a Room's Schedule ---")
            room_no = input("Enter Room ID: ").strip()
            print("--- Room Details ---")
            try:
                system.view_bookings(room_no)
            except Exception as e:
                print(e)

        elif option == "5":
            # Save everything before exiting
            print(f"Saving data to {FILENAME}...")
            system.save_data(FILENAME)
            print("Goodbye!")
            break
        else:
            print("Please enter a valid option!")
