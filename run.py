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
