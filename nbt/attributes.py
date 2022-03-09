from .__init__ import Slot, Operation
from ..abc import UUID


class EntityAttribute:
    """
    Define the attributes of an entity.
    """

    def __init__(self):
        self.attributes = []

    def __str__(self):
        output = "Attributes:["
        for i in self.attributes:
            output = output + "{" + f"Name:{i['name']},Base:{i['base']}" + "},"
        output = output[:-1] + "]"
        return output

    def max_health(self, amount: int):
        """
        Sets the max HP that an entity can regenerate to.
        """
        self.attributes.append({
            "name": "generic.max_health",
            "base": amount
        })
        return self

    def follow_range(self, amount: float):
        """
        The range which an entity will follow another entity.
        """
        self.attributes.append({
            "name": "generic.follow_range",
            "base": amount
        })
        return self

    def knockback_resistance(self, amount: float):
        """
        The chance of the knockback be cancelled.
        1.0 is 100%
        """
        self.attributes.append({
            "name": "generic.knockback_resistance",
            "base": amount
        })
        return self

    def movement_speed(self, amount: float):
        """
        The movement speed.
        """
        self.attributes.append({
            "name": "generic.movement_speed",
            "base": amount
        })
        return self

    def attack_damage(self, amount: float):
        """
        The damage inflicted.
        """
        self.attributes.append({
            "name": "generic.attack_damage",
            "base": amount
        })
        return self

    def protection(self, amount: float):
        """
        The protection amount.
        """
        self.attributes.append({
            "name": "generic.armor",
            "base": amount
        })
        return self

    def armor_toughness(self, amount: float):
        """
        Weakens critical attacks
        """
        self.attributes.append({
            "name": "generic.armor_toughness",
            "base": amount
        })
        return self

    def attack_knockback(self, amount: float):
        """
        The knockback inflicted.
        """
        self.attributes.append({
            "name": "generic.attack_knockback",
            "base": amount
        })
        return self


class ItemAttribute:
    """
    Define the attributes of an item.
    """

    def __init__(self):
        self.attributes = []

    def __str__(self):
        output = "AttributeModifiers:["
        for i in self.attributes:
            output = output + \
                     "{" + \
                     f"AttributeName:{i['name']},Name:{i['name']},Amount:{i['amount']}," + \
                     f"Operation:{i['operation']},UUID:{UUID()},Slot:{i['slot']}" + \
                     "},"
        output = output[:-1] + "]"
        return output

    def max_health(self, amount: int, operation: Operation = Operation.AMOUNT, slot: Slot = Slot.MAIN_HAND):
        """
        Sets the max HP that an entity can regenerate to.
        """
        self.attributes.append({
            "name": "generic.max_health",
            "amount": amount,
            "slot": slot,
            "operation": operation
        })
        return self

    def follow_range(self, amount: float, operation: Operation = Operation.AMOUNT, slot: Slot = Slot.MAIN_HAND):
        """
        The range which an entity will follow another entity.
        """
        self.attributes.append({
            "name": "generic.follow_range",
            "amount": amount,
            "slot": slot,
            "operation": operation
        })
        return self

    def knockback_resistance(self, amount: float, operation: Operation = Operation.AMOUNT, slot: Slot = Slot.MAIN_HAND):
        """
        The chance of the knockback be cancelled.
        1.0 is 100%
        """
        self.attributes.append({
            "name": "generic.knockback_resistance",
            "amount": amount,
            "slot": slot,
            "operation": operation
        })
        return self

    def movement_speed(self, amount: float, operation: Operation = Operation.AMOUNT, slot: Slot = Slot.MAIN_HAND):
        """
        The movement speed.
        """
        self.attributes.append({
            "name": "generic.movement_speed",
            "amount": amount,
            "slot": slot,
            "operation": operation
        })
        return self

    def attack_damage(self, amount: float, operation: Operation = Operation.AMOUNT, slot: Slot = Slot.MAIN_HAND):
        """
        The damage inflicted.
        """
        self.attributes.append({
            "name": "generic.attack_damage",
            "amount": amount,
            "slot": slot,
            "operation": operation
        })
        return self

    def protection(self, amount: float, operation: Operation = Operation.AMOUNT, slot: Slot = Slot.MAIN_HAND):
        """
        The protection amount.
        """
        self.attributes.append({
            "name": "generic.armor",
            "amount": amount,
            "slot": slot,
            "operation": operation
        })
        return self

    def armor_toughness(self, amount: float, operation: Operation = Operation.AMOUNT, slot: Slot = Slot.MAIN_HAND):
        """
        Weakens critical attacks
        """
        self.attributes.append({
            "name": "generic.armor_toughness",
            "amount": amount,
            "slot": slot,
            "operation": operation
        })
        return self

    def attack_knockback(self, amount: float, operation: Operation = Operation.AMOUNT, slot: Slot = Slot.MAIN_HAND):
        """
        The knockback inflicted.
        """
        self.attributes.append({
            "name": "generic.attack_knockback",
            "amount": amount,
            "slot": slot,
            "operation": operation
        })
        return self
