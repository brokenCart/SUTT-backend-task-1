class RoomAlreadyExistsError(Exception):
    def __init__(self, room_no):
        super().__init__(f"Room with number as '{room_no}' already exists!")

class RoomNotFoundError(Exception):
    def __init__(self, room_no):
        super().__init__(f"Room with number as '{room_no}' doesn't exists!")

class TimeslotAlreadyBookedError(Exception):
    def __init__(self, room_no, hour):
        super().__init__(f"Room with number as '{room_no}' is already booked at hour '{hour}'!")
