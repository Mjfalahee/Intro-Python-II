# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room, inventory = []):
        self.name = name 
        self.current_room = current_room
        self.inventory = inventory

    def __str__(self):
        return f"Player: {self.name}"

    def __repr__(self):
        return f'Player({repr(self.name)}, {repr(self.current_room)})'