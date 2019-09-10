from room import Room
from player import Player
from item import Item

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

# Declare all the items

item = {
    'broadsword' : Item("broadsword", "it is a large metal sword in a shiny scabbard."),
    'arrow' : Item("arrow", "it has a wooden shaft with a bone tip"),
    'pouch' : Item("pouch", "it is made of leather and clinks like metal when moved"),
    'amulet' : Item("amulet", "it is made of gold and has a large red gemstone in its center"),
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

room['foyer'].items = [item['pouch']]
room['treasure'].items = [item['amulet'], item['broadsword']]
room['narrow'].items = [item['arrow']]

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


print(f' \n \n \nWelcome to the game, {new_player.name}. This will not be an easy adventure.')
print(f'At any time, type help to see the possible commands. Good luck! \n')


while game == True:
    print(f"{room[new_player.current_room]} \n")
    if room[new_player.current_room].items != []:
        print("This room contains the following item(s): ")
        for x in room[new_player.current_room].items:
            print("~ " + str(x))

    direction = input("Please enter a command: ")
    command = direction.split(" ")

    # Handle single input commands. Travel, Help, inventory, or quit
    if len(command) == 1:
        if (direction == 'quit'):
            game = False
            pass

        if (direction == 'help'):
            print("You can enter commands to travel by typing: 'n, s, w, or e'")
            print("Take items by typing: take 'item'")
            print("You can check the items you've picked up by typing: 'inventory' or simply 'i'")
            print("You can exit the game by typing: 'quit' \n")
            destination = 'help'

        if direction == 'inventory' or direction == 'i':
            if (new_player.inventory == []):
                print('Your inventory is empty.')
                destination= 'help'
            else:
                print(f'Your inventory currently contains: \n')
                for i in new_player.inventory:
                    print(f'~~ {i} ~~')
                destination = 'help'

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
            print("\n You cannot travel that way. Choose another direction. \n")
        elif destination == 'help':
            pass

        else:
            for i in room:
                if destination == room[i]:
                    print(f"You head towards the {room[i].name}. \n")
                    new_player.current_room = i

    # Handle multiple input commands. Get() Item, remove() Item
    elif len(command) == 2:
        if command[0] == 'get' or command[0] == 'take':
            item_found = False
            for obj in room[new_player.current_room].items:
                item_found = False
                if command[1] == obj.name: #if the obj is the item in the command
                    item_found = True
                    print(f'You take the {obj.name} and put it in your inventory.')
                    room[new_player.current_room].items.remove(obj) #remove item from the room
                    new_player.inventory.append(item[obj.name])
                else:
                    item_found = False
            if not item_found:
                print(f"You didn't find the {command[1]}, try something else.")


        elif command[0] == 'drop' or command[0] == 'remove':
            item_found = False
            for obj in new_player.inventory:
                if command[1] == obj.name:
                    print(f"You remove the {obj.name} from your inventory and drop it on the ground.")
                    new_player.inventory.remove(obj)
                    room[new_player.current_room].items.append(obj)
                    item_found = True
                else:
                    item_found = False
            if not item_found:
                print("You aren't carrying that item.")
        pass



if game == False:
    print("\nThanks for playing! Please come back soon :) \n")