# Custom errors to make debugging and messages clearer

class RoomAlreadyExistsError(Exception):
    def __init__(self, room_no):
        super().__init__(f"Room with number '{room_no}' already exists!")

class RoomNotFoundError(Exception):
    def __init__(self, room_no):
        super().__init__(f"Room with number '{room_no}' does not exist!")

class TimeslotAlreadyBookedError(Exception):
    def __init__(self, room_no, hour):
        super().__init__(f"Room '{room_no}' is already booked at hour '{hour}'!")
