import test_game as tg

# Command Base Class


class Command:
    # Maybe something could be shared, so we will need this class
    def execute(self, g: tg.BoardActor) -> None:
        pass

# Simple commands here, could be like a wizard casting a spell
# according to the game


class UpCommand(Command):
    def execute(self, g: tg.BoardActor) -> None:
        g.adjust_up()


class DownCommand(Command):
    def execute(self, g: tg.BoardActor) -> None:
        g.adjust_down()


class LeftCommand(Command):
    def execute(self, g: tg.BoardActor) -> None:
        g.adjust_left()


class RightCommand(Command):
    def execute(self, g: tg.BoardActor) -> None:
        g.adjust_right()
