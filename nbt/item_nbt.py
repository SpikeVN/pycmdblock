from ..abc import JSONText, Block, Enchantment
from ..utils import text
import json

class NBT:
    """
    The base NBT of an Item.
    """

    def __init__(self):
        self.raw = "{"

    def __str__(self):
        return self.raw[:-1] + "}"

    def display(self, name: JSONText | list[JSONText] = None, lore: list[JSONText] = None):
        """
        Change the display name of the item.
        You must set italics to false, or else Minecraft will default to use italics text.
        """
        if name is None and lore is None:
            # Why would they do this for?
            return self
        if name is not None:
            self.raw = self.raw + "display:{" + f"Name:'{json.dumps(text(name), ensure_ascii=False)}'," if name is not None else ""
        if lore is not None:
            self.raw += "Lore:["
            for i in text(lore):
                self.raw = self.raw + "'" + json.dumps(i, ensure_ascii=False) + "',"
            self.raw = self.raw[:-1] + "],"
        self.raw = self.raw[:-1] + "},"
        return self

    def model_id_data(self):
        raise NotImplementedError("This feature hasn't been implemented yet.")

    def tag(self, **kwargs):
        """
        Custom tag name, with values, like jumpBoost=True, etc.
        """
        for i, v in kwargs.items():
            if " " in i:
                raise ValueError("Invalid key name.")
            if type(v) == bool:
                value = "1b" if v else "0b"
            elif type(v) == float:
                value = str(v) + "f"
            elif type(v) == int:
                value = str(v)
            else:
                raise ValueError("Invalid value.")
            self.raw += f"{i}:{value},"
        self.raw = self.raw[:-1]
        return self

    def can_place_on(self, *args: Block):
        """
        The blocks that this can place on.
        """
        self.raw += "CanPlaceOn:["
        for i in args:
            self.raw += '"' + i.type if type(i) == Block else "" + "'"
        self.raw = self.raw[:-1] + "]"
        return self

    def can_destroy(self, *args: Block):
        """
        The blocks that this can destroy.
        """
        self.raw += "CanDestroy:["
        for i in args:
            self.raw += '"' + i.type if type(i) == Block else "" + '"'
        self.raw = self.raw[:-1] + "]"
        return self

    # Again, avoids circular imports
    from .__init__ import HideFlag, ItemAttribute

    def hide_flags(self, *flags: HideFlag):
        """
        The part of the tooltip to hide.
        """
        s = 0
        for i in flags:
            s += i
        self.raw += f"HideFlags:{s},"
        return self

    def enchant(self, *enchantments: Enchantment):
        """
        The enchantments of the item.
        Input None for the 'shiny' effect without giving any actual enchantment
        """
        if enchantments is None:
            self.raw += "Enchantments:[{}],"
            return self
        self.raw += f"Enchantments:["
        for i in enchantments:
            self.raw = self.raw + "{" + f"id:\"{i.name}\",lvl:{i.level}s" + "},"
        self.raw = self.raw[:-1] + "],"
        return self

    def attributes(self, attributes: ItemAttribute):
        self.raw = self.raw + str(attributes) + ","
