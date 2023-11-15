

class BoardActor:
    def __init__(self, pos_x, pos_y) -> None:
        self._pos_x = pos_x
        self._pos_y = pos_y
        self.steps = 0
    # I know I can use one method and test on arguments or some other way but I think separation
    # in this case makes it easier and costs nothing

    def adjust_left(self):
        self._pos_x -= self.steps

    def adjust_right(self):
        self._pos_x += self.steps

    def adjust_up(self):
        self._pos_y += self.steps

    def adjust_down(self):
        self._pos_y -= self.steps


# Those are for the strategy Pattern

class Archer(BoardActor):
    """Archer always move one step"""

    def __init__(self, pos_x, pos_y) -> None:
        super().__init__(pos_x, pos_y)
        self.steps = 1

    def __str__(self) -> str:
        # bow unicode
        return '\U0001F3F9'


class Soldier(BoardActor):
    """Soldier always move two steps to get closer since he just have a short sword"""

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

    def show(self):
        print('-----' * len(self.board[0]) + '-')
        for row in self.board:
            print('|  ' + '  | '.join(row) + ' |')
            print('-----' * len(row) + '-')

    def add_actor(self, b: BoardActor):
        self.actors.append[b]
