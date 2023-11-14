from enum import Enum
import test_game as tg
# joystick where you can press 2 buttons, enumeration

# input capture solution


def get_pressed_button() -> str | None:
    b = input("Press 'w' or 'a' or 's' or 'd' :\n")
    return b if isinstance(b, JoystickEnum) else None


# The remapable joystick
class JoystickEnum(str, Enum):
    BUTTON_W = 'w'
    BUTTON_A = 'a'
    BUTTON_S = 's'
    BUTTON_D = 'd'

# Command Base Class


class Command:
    def execute(self, g: tg.BoardActor) -> None:
        pass


class UpCommand(Command):
    def execute(self, g: tg.BoardActor) -> None:
        return super().execute(g)


class DownCommand(Command):
    def execute(self, g: tg.BoardActor) -> None:
        return super().execute(g)


class LeftCommand(Command):
    def execute(self, g: tg.BoardActor) -> None:
        return super().execute(g)


class RightCommand(Command):
    def execute(self, g: tg.BoardActor) -> None:
        return super().execute(g)


class Controller():
    def __init__(self) -> None:
        self.Command_A = Command()
        self.Command_W = Command()
        self.Command_S = Command()
        self.Command_D = Command()

    def handle_pressed(self):
        p = get_pressed_button()
        if p:
            pass


gb = tg.GameBoard(11, 10)
gb.show()
