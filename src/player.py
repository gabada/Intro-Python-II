# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    """A player, their vital stats, and location"""
    def __init__(self, name, age, health, room):
        self.name = name
        self.age = age
        self.health = health
        self.room = room

    def __str__(self):
        return(f'{self.name} has health of {self.health} and is in {self.room}')

    def move(self, direction):
        self.room = self.room.n_to

