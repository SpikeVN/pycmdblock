from ..abc import *
from .addons import *
from enum import Enum


class HideFlag(Enum):
    """
    The part of the tooltip which will be hided.
    """
    ENCHANTMENTS = 1
    MODIFIERS = 2
    UNBREAKABLE = 4
    CAN_DESTROY = 8
    CAN_PLACE_ON = 16
    HIDE_OTHERS = 32
    DYED = 64


class Slot(Enum):
    MAIN_HAND = "mainhand"
    OFF_HAND = "offhand"
    HEAD = "head"
    CHEST = "chest"
    LEGS = "legs"
    FEET = "feet"


class Operation(Enum):
    AMOUNT = 0
    PERCENTAGE = 1
    MULTIPLICATIVE = 2


from .attributes import *
from .entity_nbt import *
from .item_nbt import *
