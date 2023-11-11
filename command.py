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


class Command():

    def __init__(self):
        pass

    def MoveLeft(msg):
        print("You move left,", msg)

    def MoveRight(msg):
        print("You move right,", msg)

    Mapping = {
        JoystickEnum.BUTTON_A: MoveLeft,
        JoystickEnum.BUTTON_D: MoveRight,
    }

    def Remap(self):
        pass

    def execute(self, b: JoystickEnum):
        return self.Mapping.get(b)


c = Command()
b = get_pressed_button()
if b:
    c.execute(b)(msg="You fall in a pit and die !")
