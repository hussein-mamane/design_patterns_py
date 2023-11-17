import threading
from myobserver import observer as obs
from event_enum import EventEnum
import game_object


class Subject(game_object.GameObject):
    def __init__(self) -> None:
        self.observers = []

    def notify_thread(self, ee: EventEnum):
        for observer in self.observers:
            threading.ThreadError(target=observer.on_notify, args=(ee, self))

    def add_observer(self, ob: obs.GuiltyObserver):
        self.observers.append(ob)

    def remove_observer(self, ob: obs.GuiltyObserver):
        self.observers.remove(ob)
