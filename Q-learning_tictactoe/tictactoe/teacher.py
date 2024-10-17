import random
from tictactoe.agent import sizeboard

class Teacher:
    """ 
    A class to implement a teacher that knows the optimal playing strategy.
    Teacher returns the best move at any time given the current state of the game.
    Note: things are a bit more hard-coded here, as this was not the main focus of
    the exercise so I did not spend as much time on design/style. Everything works
    properly when tested.

    Parameters
    ----------
    level : float 
        teacher ability level. This is a value between 0-1 that indicates the
        probability of making the optimal move at any given time.
    """

    def __init__(self, level=0.9):
        """
        Ability level determines the probability that the teacher will follow
        the optimal strategy as opposed to choosing a random available move.
        """
        self.ability_level = level

    def win(self, board, key='X'):
        """ If we have two in a row and the 3rd is available, take it. """
        # Check for diagonal wins
        a = [board[i][i] for i in range(sizeboard)]
        b = [board[i][(sizeboard-1) - i] for i in range(sizeboard)]
        if a.count('-') == 1 and a.count(key) == sizeboard:
            ind = a.index('-')
            return ind, ind
        elif b.count('-') == 1 and b.count(key) == sizeboard:
            ind = b.index('-')
            return ind, sizeboard - ind
        # Now check for 2 in a row/column + empty 3rd
        for i in range(sizeboard):
            row = [board[i][j] for j in range(sizeboard)]
            col = [board[j][i] for j in range(sizeboard)]
            if row.count('-') == 1 and row.count(key) == sizeboard - 1:
                return i, row.index('-')
            elif col.count('-') == 1 and col.count(key) == sizeboard - 1:
                return col.index('-'), i
        return None

    def blockWin(self, board):
        """ Block the opponent if she has a win available. """
        return self.win(board, key='O')

    def fork(self, board):
        """ Create a fork opportunity such that we have multiple threats to win. """
        for i in range(sizeboard - 1):
            for j in range(sizeboard - 1):
                if board[i][j] == 'X' and board[i+1][j+1] == 'X':
                    if board[i][j+1] == '-' and board[i+1][j] == '-':
                        return i, j+1
        return None

    def blockFork(self, board):
        """ Block the opponent's fork if they have one available. """
        return self.fork(board)

    def center(self, board):
        """ Pick the center if it is available. """
        center_pos = sizeboard // 2
        if board[center_pos][center_pos] == '-':
            return center_pos, center_pos
        return None

    def corner(self, board):
        """ Pick a corner move. """
        corners = [(0, 0), (0, sizeboard-1), (sizeboard-1, 0), (sizeboard-1, sizeboard-1)]
        # Pick opposite corner of opponent if available
        for (i, j) in corners:
            if board[i][j] == 'O' and board[sizeboard-1-i][sizeboard-1-j] == '-':
                return sizeboard-1-i, sizeboard-1-j
        # Pick any corner if no opposites are available
        for (i, j) in corners:
            if board[i][j] == '-':
                return i, j
        return None

    def sideEmpty(self, board):
        """ Pick an empty side. """
        sides = [(i, j) for i in range(sizeboard) for j in range(sizeboard) if (i == 0 or i == sizeboard-1 or j == 0 or j == sizeboard-1) and not (i == 0 and j == 0) and not (i == 0 and j == sizeboard-1) and not (i == sizeboard-1 and j == 0) and not (i == sizeboard-1 and j == sizeboard-1)]
        for (i, j) in sides:
            if board[i][j] == '-':
                return i, j
        return None

    def randomMove(self, board):
        """ Choose a random move from the available options. """
        possibles = [(i, j) for i in range(sizeboard) for j in range(sizeboard) if board[i][j] == '-']
        return possibles[random.randint(0, len(possibles)-1)]

    def makeMove(self, board):
        """
        Trainer goes through a hierarchy of moves, making the best move that
        is currently available each time. A touple is returned that represents
        (row, col).
        """
        # Chose randomly with some probability so that the teacher does not always win
        if random.random() > self.ability_level:
            return self.randomMove(board)
        # Follow optimal strategy
        a = self.win(board)
        if a is not None:
            return a
        a = self.blockWin(board)
        if a is not None:
            return a
        a = self.fork(board)
        if a is not None:
            return a
        a = self.blockFork(board)
        if a is not None:
            return a
        a = self.center(board)
        if a is not None:
            return a
        a = self.corner(board)
        if a is not None:
            return a
        a = self.sideEmpty(board)
        if a is not None:
            return a
        return self.randomMove(board)