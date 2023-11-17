import threading
import myobserver
from event_enum import EventEnum
import game_object


class Subject(game_object.GameObject):
    def __init__(self) -> None:
        self.observers = []

    def notify_thread(self, ee: EventEnum):
        for observer in self.observers:
            threading.Thread(target=observer.on_notify, args=(ee,)).start()

    def add_observer(self, ob: myobserver.Observer):
        self.observers.append(ob)

    def remove_observer(self, ob: myobserver.Observer):
        self.observers.remove(ob)

    def throw_grenade(self):
        print(EventEnum.HERO_THROW_GRENADE_EVENT.value)
        self.notify_thread(EventEnum.HERO_THROW_GRENADE_EVENT)

    def jump(self):
        print(EventEnum.HERO_JUMP_EVENT.value)
        self.notify_thread(EventEnum.HERO_JUMP_EVENT)
