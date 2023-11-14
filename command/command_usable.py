from enum import Enum
# joystick where you can press 2 buttons, enumeration


class GameBoard:
    def __init__(self, len_x, len_y) -> None:
        self.board = [[' '] * len_x for _ in range(len_y)]

    def show(self):
        print('+---' * len(self.board[0]) + '+')
        for row in self.board:
            print('| ' + ' | '.join(row) + ' |')
            print('+---' * len(row) + '+')


class BoardActor:
    def __init__(self, pos_x, pos_y, char) -> None:
        self._pos_x = pos_x
        self._pos_y = pos_y
        self._char = char


# the remapable joystick
class JoystickEnum(str, Enum):
    BUTTON_W = 'w'
    BUTTON_A = 'a'
    BUTTON_S = 's'
    BUTTON_D = 'd'


class Command:
    def __init__(self, b: JoystickEnum) -> None:
        self.button = b

    def execute(self, g: BoardActor) -> None:
        pass


class Controller():
    def __init__(self) -> None:
        pass


gb = GameBoard(5, 5)
gb.show()
