# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    """A player, their vital stats, and location"""
    def __init__(self, name, age, health, room):
        self.name = name
        self.age = age
        self.health = health
        self.room = room
        self.items = []

    def __str__(self):
        return(f'{self.name} has health of {self.health} and is in {self.room}')

    def move(self, direction):
        if direction == 'n':
            self.room = self.room.n_to
        elif direction =='e':
            self.room = self.room.e_to
        elif direction =='w':
            self.room = self.room.w_to
        elif direction =='s':
            self.room = self.room.s_to

