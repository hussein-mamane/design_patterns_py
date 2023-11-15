import inputs
import test_game as tg
import command_strategy as cs

gb = tg.GameBoard(10, 10)

archer1 = tg.Archer(2, 2)
soldier1 = tg.Soldier(3, 3)

controller = inputs.Controller()

controller.handle_pressed()
