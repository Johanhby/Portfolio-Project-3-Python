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
