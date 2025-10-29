import csv
from errors import RoomAlreadyExistsError, RoomNotFoundError, TimeslotAlreadyBookedError

START_HOUR = 0
END_HOUR = 23
HOURS = END_HOUR - START_HOUR + 1

class BookingSystem:
    def __init__(self):
        self.rooms = {}
    
    def create_room(self, room_no, building, capacity):
        if self.rooms.get(room_no):
            raise RoomAlreadyExistsError(room_no)
        room = Room(room_no, building, capacity)
        self.rooms[room_no] = room
    
    def book_room(self, room_no, hour):
        room = self.rooms.get(room_no)
        if not room:
            raise RoomNotFoundError(room_no)
        if room.booked_hours[hour]:
            raise TimeslotAlreadyBookedError(room_no, hour)
        room.booked_hours[hour] = True
    
    def filter_by_building(self, building):
        return set([room for room in self.rooms.values() if room.building == building])
    
    def filter_by_capacity(self, capacity):
        return set([room for room in self.rooms.values() if room.capacity >= capacity])
    
    def filter_by_hour(self, hour):
        return set([room for room in self.rooms.values() if not room.booked_hours[hour]])
    
    def view_bookings(self, room_no):
        room = self.rooms.get(room_no)
        if not room:
            raise RoomNotFoundError(room_no)
        print(f"ID: {room.room_no}")
        print(f"Building: {room.building}")
        print(f"Capacity: {room.capacity}")
        print(f"Booked Hours: {[i for i in range(HOURS) if room.booked_hours[i]]}")
    
    def load_data(self, filename):
        with open(filename, "r") as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                self.create_room(row["room_no"], row["building"], int(row["capacity"]))
                room = self.rooms[row["room_no"]]
                booked_hours = row["booked_hours"]
                booked_hours_list = []
                if booked_hours:
                    booked_hours = booked_hours.split(";")
                    booked_hours_list = [int(hour) for hour in booked_hours]
                for hour in booked_hours_list:
                    room.booked_hours[hour] = True
    
    def save_data(self, filename):
        with open(filename, "w") as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=["room_no", "building", "capacity", "booked_hours"])
            csv_writer.writeheader()

            for room in self.rooms.values():
                booked_hours = ";".join([str(i) for i in range(len(room.booked_hours)) if room.booked_hours[i]])
                csv_writer.writerow({"room_no": room.room_no, "building": room.building, "capacity": room.capacity, "booked_hours": booked_hours})

class Room:
    def __init__(self, room_no, building, capacity):
        self.room_no = room_no
        self.building = building
        self.capacity = capacity
        self.booked_hours = [False] * HOURS
