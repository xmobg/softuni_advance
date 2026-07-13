class Hotel:

    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        room = [room for room in self.rooms if room.number == room_number][0]
        result = room.take_room(people)
        if result is None:
            self.guests += people
        return result

    def free_room(self, room_number):
        room = [room for room in self.rooms if room.number == room_number][0]
        freed_guests = room.guests
        result = room.free_room()
        if result is None:
            self.guests -= freed_guests
        return result

    def status(self):
        free_rooms = [str(room.number) for room in self.rooms if not room.is_taken]
        taken_rooms = [str(room.number) for room in self.rooms if room.is_taken]
        return (f"Hotel {self.name} has {self.guests} total guests\n"
                f"Free rooms: {', '.join(free_rooms)}\n"
                f"Taken rooms: {', '.join(taken_rooms)}")
