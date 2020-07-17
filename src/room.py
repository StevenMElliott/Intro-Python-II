# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    n_to = None
    e_to = None
    s_to = None
    w_to = None

    def __init__(self, room, description, items=[]):
        self.room = room
        self.description = description
        self.items = items
    
    def __str__(self):
        output = f"{self.room} -- {self.description}"
        return output
