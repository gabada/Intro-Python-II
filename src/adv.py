from room import Room
from player import Player
from item import Item

# Declare all the rooms


compass = Item("Compass", "This should show you the way")
pencil = Item("Pencil", "Ordinary pencil?")
rock = Item("Rock", "Could come in handy...")
gun = Item("Gun", "Keep this at arms reach!")
hammer = Item("Hammer", "Keep this at arms reach!")
money = Item("Money", "Don't waste time counting")
telescope = Item("Telescope", "Can you see anything nice?")
gold = Item("Gold", "Is it real?")
crowbar = Item("Crowbar", "Do you have a use for this?")
donut = Item("Donut", "A little pick me up")
shakles = Item("Shakles", "From escapes prisoners")
teeth = Item("Teeth", "Teeth on the floor... gross")
flares = Item("Flares", "Still have that gun?")
ladder = Item("Ladder", "Is it long enough ")
rope = Item("Rope", "Maybe its long enough to get down?")

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [compass]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [pencil, rock, gun]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [hammer, money, telescope] ),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [gold]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [crowbar, donut]),
    'dungeon': Room("The Dungeon", """You've fallen into the dungeon! There are
skeletons everywhere. Try to get out by going south!""", [shakles, teeth]),
    'roof': Room("The Roof", """You escaped the house! You are on the roof! Not sure
how you will leave though... Have a flare gun? Please don't jump off our roof""", [flares, ladder, rope]),
}

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']
room['narrow'].s_to = room['dungeon']
room['dungeon'].s_to = room['roof']
room['roof'].n_to = room['outside']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player1_name = input('What is your Name? ')
print('')
player1_age = input('How old are you? ')


current_player = Player(player1_name, player1_age, 100, room['outside'], None)
valid_directions = ('n','e','w','s')
valid_items = ('compass','pencil', 'rock','gun','hammer','money','telescope','gold',
    'crowbar','donut','shakles','teeth', 'flares', 'ladder', 'rope')

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

def invalid():
    print(f'Invalid Direction! You are currently {current_player.current_room.name}\n')
    direction = input(f'Where would you like to go? ')


while True:
    print(f'You are currently in {current_player.current_room.name}\n')
    print('To pick up or drop an item just enter the name of the item you see!\n')
    print(f'{current_player.current_room.description}, Items: {", ".join([item.name for item in current_player.current_room.items])}\n')
    direction = input(f'What now? ')
    if direction.lower() in valid_directions:
        try:
            current_player.move(direction)
            print(f'{current_player.current_room.name}')
        except:
            invalid()
    elif direction.lower() == 'q':
        print('Thanks for playing!\n')
        break
    elif direction.lower() in valid_items and 'get' or 'drop':
        if direction.lower().split()[1] == 'compass':
            try:
                current_player.pickup(compass)
            except:
                print('That item is too far away!\n')
        elif direction.lower().split()[1] == 'pencil':
            try:
                current_player.pickup(pencil)
            except:
                print('That item is too far away!\n')
        elif direction.lower().split()[1] == 'rock':
            try:
                current_player.pickup(rock)
            except:
                print('That item is too far away!\n')
        elif direction.lower().split()[1] == 'gun':
            try:
                current_player.pickup(gun)
            except:
                print('That item is too far away!\n')
        elif direction.lower().split()[1] == 'hammer':
            try:
                current_player.pickup(hammer)
            except:
                print('That item is too far away!\n')
        elif direction.lower().split()[1] == 'money':
            try:
                current_player.pickup(money)
            except:
                print('That item is too far away!\n')
        elif direction.lower().split()[1] == 'telescope':
            try:
                current_player.pickup(telescope)
            except:
                print('That item is too far away!\n')
        elif direction.lower().split()[1] == 'gold':
            try:
                current_player.pickup(gold)
            except:
                print('That item is too far away!\n')
        elif direction.lower().split()[1] == 'crowbar':
            try:
                current_player.pickup(crowbar)
            except:
                print('That item is too far away!\n')
        elif direction.lower().split()[1] == 'donut':
            try:
                current_player.pickup(donut)
            except:
                print('That item is too far away!\n')
        elif direction.lower().split()[1] == 'shakles':
            try:
                current_player.pickup(shakles)
            except:
                print('That item is too far away!\n')
        elif direction.lower().split()[1] == 'teeth':
            try:
                current_player.pickup(teeth)
            except:
                print('That item is too far away!\n')
        elif direction.lower().split()[1] == 'flares':
            try:
                current_player.pickup(flares)
            except:
                print('That item is too far away!\n')
        elif direction.lower() == 'ladder':
            try:
                current_player.pickup(ladder)
            except:
                print('That item is too far away!\n')
        elif direction.lower() == 'rope':
            try:
                current_player.pickup(rope)
            except:
                print('That item is too far away!\n')
        else:
            print('That item is too heavy to pick up!')
    else:
        invalid()