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

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
new_player = Player("Frank", 'outside')

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


# defining variables
game = True
destination = None
direction = None


print(f'Welcome to the game, {new_player.name}. This will not be an easy adventure. \n')


while game == True:
    print(f"{room[new_player.current_room]} \n")
    direction = input("Please enter a direction to travel in (n, e, s, w): ")

    if (direction == 'quit'):
        game = False
        pass

    elif (direction == 'n'):
        destination = room[new_player.current_room].n_to
    elif (direction == 'e'):
        destination = room[new_player.current_room].e_to
    elif (direction == 'w'):
        destination = room[new_player.current_room].w_to
    elif (direction == 's'):
        destination = room[new_player.current_room].s_to
    else:
        print("You must enter a valid direction in order to travel.")

    if destination == None:
        print("You cannot travel that way. Choose another direction.")
    else:
        for i in room:
            if destination == room[i]:
                print(f"You head towards the {room[i].name}. \n")
                new_player.current_room = i



if game == False:
    print("\nThanks for playing! Please come back soon :) \n")