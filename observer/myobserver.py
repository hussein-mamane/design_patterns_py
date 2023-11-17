import pickle
import os
import game_object
import event_enum


class observer:
    def __init__(self) -> None:
        if os.path.exists('gamer_successes.pickle'):
            with open('gamer_successes.pickle', 'rb') as file:
                self.success_dict = pickle.dump(file)
        else:
            self.success_dict = dict()
            self.success_dict['nb_grenade_victims'] = 0
            self.success_dict['nb_jumps'] = 0

    def on_notify(self, g: game_object.GameObject, e: event_enum.EventEnum):
        if self.success_dict['nb_grenade_victims'] < 10:
            # no test on g, it is a Subject who can throw this kind of event
            # so it should be something we can handle for its class
            if e == event_enum.EventEnum.HERO_THROW_GRENADE_EVENT:
                self.success_dict['nb_grenade_victims'] += 1
                if self.success_dict['nb_grenade_victims'] == 10:
                    print("\Success: Grenade Maniac : Throw 10 successful grenades !\n")
