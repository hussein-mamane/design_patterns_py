import inputs
import test_game as tg
import command_pattern as cp

gb = tg.GameBoard(5, 5)

archer1 = tg.Archer(2, 2)
thief1 = tg.Thief(3, 3)

controller = inputs.Controller()
gb.add_actor(archer1)
gb.add_actor(thief1)
gb.update_board()

b: inputs.Button = None
# ctrl+c to quit

while True:
    gb.show()
    print('Move the  archer:\n')
    b = controller.handle_pressed()
    b._command.execute(archer1)
    print('Move the  thief:\n')
    b = controller.handle_pressed()
    b._command.execute(thief1)
    gb.update_board()
