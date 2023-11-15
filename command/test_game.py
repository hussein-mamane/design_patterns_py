

class BoardActor:
    def __init__(self, pos_x, pos_y) -> None:
        self._pos_x = pos_x
        self._pos_y = pos_y
        self.steps = 0
    # I know I can use one method and test on arguments or some other way but I think separation
    # in this case makes it easier and costs nothing

    def adjust_left(self):
        self._pos_x -= self.steps
        # using the modulus to stay in bounds of the 5*5 board
        self._pos_x = self._pos_x//5

    def adjust_right(self):
        self._pos_x += self.steps
        self._pos_x = self._pos_x//5

    def adjust_up(self):
        self._pos_y += self.steps
        self._pos_y = self._pos_y//5

    def adjust_down(self):
        self._pos_y -= self.steps
        self._pos_y = self._pos_y//5


# Those are for the strategy Pattern

class Archer(BoardActor):
    """Archers always move one step"""

    def __init__(self, pos_x, pos_y) -> None:
        super().__init__(pos_x, pos_y)
        self.steps = 1

    def __str__(self) -> str:
        # bow unicode
        return '\U0001F3F9'


class Thief(BoardActor):
    """Thieves always move two steps to get closer since he just have a dagger"""

    def __init__(self, pos_x, pos_y) -> None:
        super().__init__(pos_x, pos_y)
        self.steps = 2

    def __str__(self) -> str:
        # dagger unicode
        return '\U0001F5E1'


class GameBoard:

    def __init__(self, len_x, len_y) -> None:
        self.board = [[' '] * len_x for _ in range(len_y)]
        self.actors = []
        self.lx = len_x
        self.ly = len_y

    def show(self):
        print('-----' * len(self.board[0]) + '-')
        for row in self.board:
            print('|  ' + '  | '.join(row) + ' |')
            print('-----' * len(row) + '-')

    def add_actor(self, ba: BoardActor):
        self.actors.append(ba)

    def update_board(self):
        # clean first
        # self.board = [[' ' for _ in range(self.lx)] for _ in range(self.ly)]
        for i in range(self.lx):
            for j in range(self.ly):
                self.board[i][j] = ' '
        for a in self.actors:
            # I do not handle when two characters get on the same case
            # as this require additionnal logic #TODO
            self.board[a._pos_x][a._pos_y] = a.__str__()
