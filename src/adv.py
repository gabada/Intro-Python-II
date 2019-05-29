from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
    'dungeon': Room("The Dungeon", """You've fallen into the dungeon! There are
     skeletons everywhere. Try to get out by going south!"""),
    'roof': Room("The Roof", """You escaped the house! You are on the roof! Not sure
    how you will leave though... Have a flare gun? Please don't jump off our roof"""),
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


current_player = Player(player1_name, player1_age, 100, room['outside'])
valid_directions = ['n','e','w','s']

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
    print('')
    print(f'Invalid Direction! You are currently in {current_player.room.name}')
    print('')
    direction = input(f'Where would you like to go? ')
    print('')


while True:
    print(f'You are currently in {current_player.room.name}')
    print('')
    print(f'{current_player.room.description}')
    print('')
    direction = input(f'Where would you like to go? ')
    print('')
    if direction.lower() in valid_directions:
        try:
            current_player.move(direction)
            print(f'{current_player.room.name}')
            print('')
        except:
            invalid()
    elif direction.lower() == 'q':
        print('')
        print('Thanks for playing!')
        break
    else:
        invalid()