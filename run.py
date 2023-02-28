from random import randint

class Board:
    def __init__(self):
        self.column = []
        self.row = []
        self.struck_locations = []
        self.ships = []

    def create_board(self):
        for y in range(5):
            self.row = []
            for x in range(5):
                self.row.append('O')
            self.column.append(self.row)

"""
A function that uses a while loop to create 5 ships randomly using the randint method and an if statement to check that the chosen coordinates do not already exist in the tuple self.ships.
"""

    def create_ships(self):
        self.ships = []
        while len(self.ships) < 5:
            ship_row = randint(0, 4)
            ship_column = randint(0, 4)
            if (ship_row, ship_column) not in self.ships:
                self.ships.append((ship_row, ship_column))

"""
A function with while loops asking for input for strike coordinates. Another nested while loop validates input and prints an error message if invalid coordinates are chosen.
"""

    def strike_location(self):
        while True:
            self.strike_row = input('Please select a ship row between numbers 1-5 to strike')
            while self.strike_row not in '12345':
                print('Please enter a valid number between 1-5')
                self.strike_row = input('Please select a ship row between 1-5 to strike')
                break

        while True:
            self.strike_column = input('Please select a ship column between numbers 1-5 to strike')
            while self.strike_column not in '12345':
                print('Please enter a valid number between 1-5')
                self.strike_column = input('Please select a ship column between 1-5 to strike')
                break

# Converting input to integer and subtracts 1 to account for 0 indexing.

        row = int(self.strike_row) - 1
        column = int(self.strike_column) - 1

# If statement to return player to prompt if previously chosen coordinates are entered.

        if not self.already_struck(row, column):
            return row, column

    def already_struck(self, row, column):
        if (row, column) in self.struck_locations:
            print('You have already struck this location')
            return True
        else:
            return False           
                        
