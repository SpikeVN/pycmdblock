import json
import random

from enum import Enum


class Dimension(Enum):
    """
    Represents a Minecraft dimension.
    """

    OVERWORLD = "minecraft:overworld"
    NETHER = "minecraft:the_nether"
    END = "minecraft:the_end"


class JSONText:
    """
    A JSON text element that allows formatting.
    Minecraft: Java Edition 1.13+
    """

    def __init__(
            self,
            raw: dict | list,
            text: str = "",
            color: str = "",
            bold: bool = False,
            italic: bool = False,
            underline: bool = False,
            strikethrough: bool = False,
            reset: bool = False,
    ):
        self.raw = raw
        self.text = text
        self.color = color
        self.bold = bold
        self.italic = italic
        self.underline = underline
        self.strikethrough = strikethrough
        self.reset = reset

    def __str__(self):
        return json.dumps(self.raw, ensure_ascii=False)


class Position:
    """
    Represents a coordinates value with x, y, z values.
    """

    def __init__(self, x: int = None, y: int = None, z: int = None, dimension: Dimension = Dimension.OVERWORLD):
        if x is None and y is None and z is None:
            self.x = "~",
            self.y = "~",
            self.z = "~"
            self.dimension = Dimension.OVERWORLD
        else:
            self.x = x
            self.y = y
            self.z = z
            self.dimension = dimension

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z and self.dimension == other.dimension

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        return f"{self.x} {self.y} {self.z}"


class Volume:
    """
    Represents a cube.
    """

    def __init__(self, x: float, y: float, z: float, dx: float, dy: float, dz: float):
        self.x = x
        self.y = y
        self.z = z
        self.dx = dx
        self.dy = dy
        self.dz = dz
        self.x2 = x + dx
        self.y2 = y + dy
        self.z2 = z + dz


class UUID:
    """
    A Universal Unique Identifier.
    Looks like this: 069a79f4-44e9-4726-a5be-fca90e38aaf5
    """

    def __init__(self, data: list[str] = None):
        if type(data) == list[str]:
            self.uuid = data
        elif data is None:
            self.random()
        else:
            raise SyntaxError("Unexpected UUID format.")

    def __str__(self):
        return f"[I;{self.uuid[0]},{self.uuid[1]},{self.uuid[2]},{self.uuid[3]}]"

    def random(self):
        """
        Generate a random UUID.
        """
        self.uuid = [
            random.randint(-9999999999, 9999999999),
            random.randint(-9999999999, 9999999999),
            random.randint(-9999999999, 9999999999),
            random.randint(-9999999999, 9999999999)
        ]


class Entity:
    """
    Represents an entity in Minecraft.
    """

    def __init__(
            self,
            entity_type: str,
            nbt
    ):
        if ":" not in entity_type:
            self.type = f"minecraft:{entity_type}"
        else:
            self.type = entity_type
        self.nbt = nbt


class Item:
    """
    Represents a Minecraft Item.
    """

    def __init__(
            self,
            name: str,
            nbt="{}",
            amount: int = 1,
    ):
        if ":" not in name:
            self.name = f"minecraft:{name}"
        else:
            self.name = name
        self.nbt = nbt
        self.amount = amount


class Block:
    """
    A block in Minecraft
    """

    def __init__(self, block_type: str, nbt=None):
        if nbt is None:
            nbt = {}
        if ":" not in block_type:
            self.name = f"minecraft:{block_type}"
        else:
            self.type = block_type
        self.nbt = nbt


class Enchantment:
    """
    Represents an enchantment.
    """

    def __init__(self, name: str, level: int = 1):
        if ":" not in name:
            self.name = f"minecraft:{name}"
        else:
            self.name = name
        self.level = level
