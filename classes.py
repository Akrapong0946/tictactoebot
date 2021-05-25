class Game:
    def __init__(self, firstturn):
        self.board = Board()
        firstturn = firstturn.strip().lower()
        self.turn = firstturn
        self.firstturn = firstturn
        self.players = {'x': None, 'o': None}

    def is_over(self):
        '''
        Checks if the game is over. Returns a boolean
        '''
        # when the board is filled
        if self.board.is_filled():
            return True

        # when the board has a strike
        elif self.board.has_strike():
            return True

        # game is not over
        else:
            return False

    def newgame(self, firstturn):
        '''
        Prepares for a new game. Takes in arguments "x" (start with player "x"), "o" (start with player "o") and "a" (continue from first game in an alternating pattern).
        '''
        self.board.clear()
        firstturn = firstturn.strip().lower()
        if firstturn == 'a':
            if self.firstturn == 'x':
                self.turn = 'o'
            else:
                self.turn = 'x'

    def nextturn(self):
        '''
        Passes the turn to the other player.
        '''
        if self.turn == 'x':
            self.turn = 'o'
        else:
            self.turn = 'x'

    def display_board(self):
        '''
        Displays the board.
        '''
        board = self.board
        return (f'\n⠀⠀–––––––––––––\n 3   |  **{board.a3}**  |  **{board.b3}**  |  **{board.c3}**  |\n      –––––––––––––\n 2   |  **{board.a2}**  |  **{board.b2}**  |  **{board.c2}**  |\n      –––––––––––––\n 1    |  **{board.a1}**  |  **{board.b1}**  |  **{board.c1}**  |\n      –––––––––––––\n        a       b       c\n')

    def end(self):
        '''
        Announces result and prompts for a new game.
        '''
        # announce result
        # no winner
        if self.board.is_filled() and (not self.board.has_strike()):
            return ('**It\'s a draw!**\nType "!start" to play again.')
        # has winner
        elif self.board.has_strike():
            return (f'**Player {self.turn} wins! Congrats!**\nType "!start" to play again.')

    def update(self, cell):
        '''
        Fills input cell with the current turn.
        '''
        cell = cell.strip().lower()

        # handle cell occupied
        # if not self.board.cell_empty(cell):
        #     raise CellOccupiedError

        if cell == 'a1':
            self.board.a1 = self.turn
        elif cell == 'a2':
            self.board.a2 = self.turn
        elif cell == 'a3':
            self.board.a3 = self.turn
        elif cell == 'b1':
            self.board.b1 = self.turn
        elif cell == 'b2':
            self.board.b2 = self.turn
        elif cell == 'b3':
            self.board.b3 = self.turn
        elif cell == 'c1':
            self.board.c1 = self.turn
        elif cell == 'c2':
            self.board.c2 = self.turn
        elif cell == 'c3':
            self.board.c3 = self.turn


class Board:
    def __init__(self):
        self.a1 = '⠀'
        self.a2 = '⠀'
        self.a3 = '⠀'
        self.b1 = '⠀'
        self.b2 = '⠀'
        self.b3 = '⠀'
        self.c1 = '⠀'
        self.c2 = '⠀'
        self.c3 = '⠀'

    def has_strike(self):
        '''
        Checks if there is a strike. Returns a boolean.
        '''
        return ((self.a1 == self.a2 == self.a3 != '⠀')
        or (self.b1 == self.b2 == self.b3 != '⠀')
        or (self.c1 == self.c2 == self.c3 != '⠀')
        or (self.a1 == self.b1 == self.c1 != '⠀')
        or (self.a2 == self.b2 == self.c2 != '⠀')
        or (self.a3 == self.b3 == self.c3 != '⠀')
        or (self.a1 == self.b2 == self.c3 != '⠀')
        or (self.a3 == self.b2 == self.c1 != '⠀'))

    def is_filled(self):
        '''
        Checks if the board is filled. Returns a boolean.
        '''
        return ((self.a1 != '⠀')
        and (self.a2 != '⠀')
        and (self.a3 != '⠀')
        and (self.b1 != '⠀')
        and (self.b2 != '⠀')
        and (self.b3 != '⠀')
        and (self.c1 != '⠀')
        and (self.c2 != '⠀')
        and (self.c3 != '⠀'))

    def clear(self):
        '''
        Empties the board to prepare for a new game.
        '''
        self.a1 = '⠀'
        self.a2 = '⠀'
        self.a3 = '⠀'
        self.b1 = '⠀'
        self.b2 = '⠀'
        self.b3 = '⠀'
        self.c1 = '⠀'
        self.c2 = '⠀'
        self.c3 = '⠀'       

    def cell_empty(self, cell):
        '''
        Checks if the input cell is empty. Returns a boolean.
        '''
        if cell == 'a1':
            return (self.a1 == '⠀')
        elif cell == 'a2':
            return (self.a2 == '⠀')
        elif cell == 'a3':
            return (self.a3 == '⠀')
        elif cell == 'b1':
            return (self.b1 == '⠀')
        elif cell == 'b2':
            return (self.b2 == '⠀')
        elif cell == 'b3':
            return (self.b3 == '⠀')
        elif cell == 'c1':
            return (self.c1 == '⠀')
        elif cell == 'c2':
            return (self.c2 == '⠀')
        elif cell == 'c3':
            return (self.c3 == '⠀')

openingstatement = '**Welcome to Tic-Tac-Toe!**\n\nBefore we begin, let me introduce you to the commands:\n\n`!start`⠀⠀⠀⠀⠀⠀⠀⠀⠀  Starts TicTacToe game on the channel\n`!p <cell_index>`⠀⠀⠀Places an "x" or "o" in the cell at <cell_index> (square coordinates)\n`!quit`⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀Force-quits the ongoing TicTacToe game'