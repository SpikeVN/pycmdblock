import utils
import json
import worker


class JsonText:
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
        return json.dumps(self.raw)


class Position:
    """
    Represents a coordinates value with x, y, z values.
    """
    HERE = "~ ~ ~"

    def __init__(self, x: int, y: int, z: int):
        self.x = x
        self.y = y
        self.z = z

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


def conv(text: str, esc="&"):
    """
    Returns the JSON rich text format from old formatted strings.
    Java Edition 1.13+ only.

    - text: The text to convert.
    - esc: The escape character. Can be anything, default is '&'
    """
    output = []
    raw = utils.convert(text, esc=esc)
    if type(raw) == list:
        for e in raw:
            a = JsonText(
                raw=raw,
                text=e["text"],
                color=e["color"],
                bold=e["bold"] if e.keys().__contains__("bold") else False,
                italic=e["italic"] if e.keys().__contains__("italic") else False,
                underline=e["underline"] if e.keys().__contains__("underline") else False,
                strikethrough=e["strikethrough"] if e.keys().__contains__("strikethrough") else False,
                reset=e["reset"] if e.keys().__contains__("reset") else False
            )
            output.append(a)
    else:
        e = raw
        return JsonText(
            raw=raw,
            text=e["text"],
            color=e["color"],
            bold=e["bold"] if e.keys().__contains__("bold") else False,
            italic=e["italic"] if e.keys().__contains__("italic") else False,
            underline=e["underline"] if e.keys().__contains__("underline") else False,
            strikethrough=e["strikethrough"] if e.keys().__contains__("strikethrough") else False,
            reset=e["reset"] if e.keys().__contains__("reset") else False
        )
    return output


def say(text: str):
    """
    Sends a message to the chat as the command executor.
    """
    worker.construct(f"say {text}")


# Avoids circular imports
import target_selector


def tellraw(target: target_selector.Target, text: list[JsonText] | JsonText):
    worker.construct(f"tellraw {target} {text}")
