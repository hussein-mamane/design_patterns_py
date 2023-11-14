from enum import Enum


# joystick where you can press 2 buttons, enumeration
class JoystickEnum(str, Enum):
    BUTTON_A = 'a'
    BUTTON_D = 'd'


# this should be in a game loop, using the engine equivalent
# input capture solution
def get_pressed_button() -> str | None:
    b = input("Press 'a' or 'd' :\n")
    return b if b == JoystickEnum.BUTTON_A\
        or b == JoystickEnum.BUTTON_D else None

# Executed movements


def MoveLeft(msg: str):
    print("You move left,", msg)


def MoveRight(msg):
    print("You move right,", msg)

# logic + data for handling input


class CommandHandler:

    def __init__(self):
        pass

    # remapping buttons
    Mapping = {
        JoystickEnum.BUTTON_A: MoveLeft,
        JoystickEnum.BUTTON_D: MoveRight,
    }

    def Remap(self):
        b = input(" 'a' or  'd' for moving left:\n")
        if b == JoystickEnum.BUTTON_A:
            self.Mapping[b] = MoveLeft
            self.Mapping[JoystickEnum.BUTTON_D] = MoveRight
        elif b == JoystickEnum.BUTTON_D:
            self.Mapping[b] = MoveLeft
            self.Mapping[JoystickEnum.BUTTON_A] = MoveRight
        else:
            print("press 'a' or 'd' only")

    def execute(self, b: JoystickEnum):
        return self.Mapping.get(b)


# test for this file standalone execution,it works
"""
c = CommandHandler()
c.Remap()

b = get_pressed_button()
if b:
    c.execute(b)("You fall in a pit and Die !")
"""
