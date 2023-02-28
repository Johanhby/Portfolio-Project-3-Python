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

    def create_ships(self):
        self.ships = []
        while len(self.ships) < 5:
            ship_row = randint(0, 4)
            ship_column = randint(0, 4)
            if (ship_row, ship_column) not in self.ships:
                self.ships.append((ship_row, ship_column))

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

        row = int(self.strike_row) - 1
        column = int(self.strike_column) - 1
        return row, column        
                        
