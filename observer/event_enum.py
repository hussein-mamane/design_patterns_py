from enum import Enum


class EventEnum(Enum, str):
    HERO_JUMP_EVENT = 'You jump\n'
    HERO_THROW_GRENADE_EVENT = 'You throw a grenade\n'
