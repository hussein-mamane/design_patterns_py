from enum import Enum
import command_pattern as cp
# joystick where you can press 2 buttons, enumeration

# input capture solution


def get_pressed_button() -> str | None:
    b = input("Press 'w' or 'a' or 's' or 'd' :\n")
    return b  # if isinstance(b, JoystickEnum) else None


# The remapable joystick


class JoystickEnum(str, Enum):
    BUTTON_W = 'w'
    BUTTON_A = 'a'
    BUTTON_S = 's'
    BUTTON_D = 'd'


class Button:
    def __init__(self, j: JoystickEnum) -> None:
        self.key = j

    def set_command(self, command: cp.Command):
        self._command = command


class Controller():
    def __init__(self) -> None:
        self.button_W = Button('w')
        self.button_A = Button('a')
        self.button_S = Button('s')
        self.button_D = Button('d')
        # Set commands, maybe a mapping table is better,
        # Like this, in case of remapping one command we have
        # to loop through all commands to remove the old mapping
        # of that command
        self.button_W.set_command(cp.UpCommand())
        self.button_A.set_command(cp.LeftCommand())
        self.button_S.set_command(cp.DownCommand())
        self.button_D.set_command(cp.RightCommand())

    def handle_pressed(self):
        p = get_pressed_button()
        print(p, "is pressed")
        if p:
            if p == JoystickEnum.BUTTON_A:
                return self.button_A
            if p == JoystickEnum.BUTTON_W:
                return self.button_W
            if p == JoystickEnum.BUTTON_S:
                return self.button_S
            if p == JoystickEnum.BUTTON_D:
                return self.button_D
