from random import randint

player_score = 0
computer_score = 0

class Board:
    def __init__(self):
        self.column = []
        self.row = []
        self.struck_locations = []
        self.ships = []

"""
A function to create a 2d 5x5 game board.
"""

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

"""
A function to determine if the strike was a hit or a miss.
"""

    def hit_or_miss(self, row, column):
        if (row, column) in self.ships:
            print("You struck a ship!")
            self.ships.remove((row, column))
            self.column[row][column] = '@'
            return True
        else:
            print("You missed!")
            self.column[row][column] = 'X'
            return False

# Increments the score of the player by 1 point in case of a hit.

    def increment_score(self):
        player_score = 0
        for row in self.column:
            for column in row:
                if column == '@':
                    player_score += 1
        return player_score

# Increments the score of the computer by 1 point in case of a hit.

    def increment_score(self):
        computer_score = 0
        for row in self.column:
            for column in row:
                if column == '@':
                    computer_score += 1
        return computer_score                               
                        
