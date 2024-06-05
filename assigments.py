class Building:
    def _init_(self, name, location):
        # Initialize a building with a name, location, and an empty list of rooms
        self.name = name
        self.location = location
        self.rooms = []

    def add_room(self, room):
        # Add a room to the building's list of rooms
        self.rooms.append(room)


class AcademicBuilding(Building):
    def _init_(self, name, location):
        # Initialize an academic building with a name, location, and a building type attribute
        super()._init_(name, location)
        self.building_type = "Academic"


class ResidentialBuilding(Building):
    def _init_(self, name, location):
        # Initialize a residential building with a name, location, and a building type attribute
        super()._init_(name, location)
        self.building_type = "Residential"


class AdministrativeBuilding(Building):
    def _init_(self, name, location):
        # Initialize an administrative building with a name, location, and a building type attribute
        super()._init_(name, location)
        self.building_type = "Administrative"


class Room:
    def _init_(self, capacity, room_type):
        # Initialize a room with a capacity, room type, and an empty list of occupants
        self.capacity = capacity
        self.room_type = room_type
        self.occupants = []


class Classroom(Room):
    def _init_(self, capacity):
        # Initialize a classroom with a capacity and a room type attribute
        super()._init_(capacity, "Classroom")


class Laboratory(Room):
    def _init_(self, capacity):
        # Initialize a laboratory with a capacity and a room type attribute
        super()._init_(capacity, "Laboratory")


class LivingRoom(Room):
    def _init_(self, capacity):
        # Initialize a living room with a capacity and a room type attribute
        super()._init_(capacity, "Living Room")


class Person:
    def _init_(self, name, id):
        # Initialize a person with a name and an ID
        self.name = name
        self.id = id


class Student(Person):
    def _init_(self, name, id):
        # Initialize a student with a name, an ID, and a role attribute
        super()._init_(name, id)
        self.role = "Student"


class Faculty(Person):
    def _init_(self, name, id):
        # Initialize a faculty member with a name, an ID, and a role attribute
        super()._init_(name, id)
        self.role = "Faculty"


class Staff(Person):
    def _init_(self, name, id):
        # Initialize a staff member with a name, an ID, and a role attribute
        super()._init_(name, id)
        self.role = "Staff"
