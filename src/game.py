from defs import *

class Game:
    def __init__(self):
        self.board = []
        self.initBoard(self.board)
        self.state = True

    def initBoard(self, board):
        for i in range(ROWS):
            self.board.append(BG * COLS)
            self.board.append('\b' + '\n')
    
    def printBoard(self):
        board = self.board
        for i in range(len(board)):
            print(board[i], end='')