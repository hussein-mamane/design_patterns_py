from subject import Subject
import myobserver

subject = Subject()
obs = myobserver.Observer()
subject.add_observer(obs)

answer: int
while True:
    answer = input(
        'What do you want to do ?\n1-throw grenade\n2-jump\n3-save progress\n4-reset progress\n')
    if answer == '1':
        subject.throw_grenade()
    elif answer == '2':
        subject.jump()
    elif answer == '3':
        obs.save_progress()
    elif answer == '4':
        obs.reset_progress()
    else:
        # easy way to make people not mess with bad input
        exit()
