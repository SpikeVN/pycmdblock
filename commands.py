from . import utils
from . import worker


def conv(text: str, esc="&"):
    """
    Returns the JSON rich text format from old formatted strings.
    Java Edition 1.13+ only.

    - text: The text to convert.
    - esc: The escape character. Can be anything, default is '&'
    """
    output = []
    raw = utils.convert(text, esc=esc)
    if type(raw) != list:
        raw = [raw]
    for e in raw:
        a = JSONText(
            raw=e,
            text=e["text"],
            color=e["color"],
            bold=e.get("bold", False),
            italic=e.get("italic", False),
            underline=e.get("underline", False),
            strikethrough=e.get("strikethrough", False),
            reset=e.get("reset", False)
        )
        output.append(a)
    return output


def say(text: str):
    """
    Sends a message to the chat as the command executor.
    """
    worker.construct(f"say {text}")


# Avoids circular imports
# from .target_selector import Target
from .nbt import *


def tellraw(target: any, text: list[JSONText] | JSONText):
    txt = []
    for i in text:
        txt.append(i.raw)
    worker.construct(f"tellraw {target} {txt}")


def summon(entity: Entity, at: Position = "~ ~ ~"):
    worker.construct(f"summon {entity.type} {at} {entity.nbt}")
