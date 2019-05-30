# Write a class to hold player information, e.g. what room they are in
# currently.
# from room import Room


class Player():
    """A player, their vital stats, and location"""
    def __init__(self, name, age, health, current_room, items):
        self.name = name
        self.age = age
        self.health = health
        self.current_room = current_room
        self.items = []

    def __str__(self):
        return(f'{self.name} has health of {self.health} and is in {self.current_room}')

    def move(self, direction):
        if direction == 'n':
            self.current_room = self.current_room.n_to
        elif direction =='e':
            self.current_room = self.current_room.e_to
        elif direction =='w':
            self.current_room = self.current_room.w_to
        elif direction =='s':
            self.current_room = self.current_room.s_to


    def pickup(self, item):
        if item in self.items:
            self.current_room.items.append(item)
            self.items.remove(item)
            print(f'You just dropped {item}\n')
        else:
            self.items.append(item)
            self.current_room.items.remove(item)
            print(f'You just picked up {item}\n')
