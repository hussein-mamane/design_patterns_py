import pickle
import os
import event_enum


class Observer:
    def __init__(self) -> None:
        if os.path.exists('gamer_successes.pickle'):
            with open('gamer_successes.pickle', 'rb') as file:
                self.success_dict = pickle.load(file)
        else:
            self.success_dict = dict()
            self.success_dict['nb_grenade_victims'] = 0
            self.success_dict['nb_jumps'] = 0

    def on_notify(self, e: event_enum.EventEnum):
        # Usually also pass the game object who notified as parameter
        if self.success_dict['nb_grenade_victims'] < 5:
            if e == event_enum.EventEnum.HERO_THROW_GRENADE_EVENT:
                self.success_dict['nb_grenade_victims'] += 1
                if self.success_dict['nb_grenade_victims'] == 5:
                    # No console api to call, No cloud database to write :(
                    # Just print
                    print(
                        "Success: \U0001F4A3Grenade Maniac!\U0001F4A3 : You threw 5 successful grenades !\n")
        if self.success_dict['nb_jumps'] < 5:
            if e == event_enum.EventEnum.HERO_JUMP_EVENT:
                self.success_dict['nb_jumps'] += 1
                if self.success_dict['nb_jumps'] == 5:
                    print(
                        "Success: \U0001F998Kangaroo!\U0001F998 : You jumped 5 times!\n")

    def reset_progress(self):
        self.success_dict['nb_grenade_victims'] = 0
        self.success_dict['nb_jumps'] = 0
        with open('gamer_successes.pickle', 'wb') as file:
            pickle.dump(self.success_dict, file)

    def save_progress(self):
        with open('gamer_successes.pickle', 'wb') as file:
            pickle.dump(self.success_dict, file)
