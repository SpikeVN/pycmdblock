color = {
    "0": "black",
    "1": "dark_blue",
    "2": "dark_green",
    "3": "dark_aqua",
    "4": "dark_red",
    "5": "dark_purple",
    "6": "gold",
    "7": "gray",
    "8": "dark_gray",
    "9": "blue",
    "a": "green",
    "b": "aqua",
    "c": "red",
    "d": "light_purple",
    "e": "yellow",
    "f": "white"
}
formatting = {
    "k": "obfuscated",
    "l": "bold",
    "m": "strikethrough",
    "n": "underline",
    "o": "italic",
    "r": "reset"
}
properties = {
    "text": "",
    "color": None,
    "bold": False,
    "italic": False,
    "underline": False,
    "strikethrough": False,
    "obfuscated": False
    # Not yet implemented
    # "click_event": None,
    # "hover_event": None
}


def new_entry(sector: dict, trying: str) -> bool:
    """
    Checks if the text need a new entry.
    """
    return sector["color"] is not None and color.__contains__(trying)


def convert(text: str, esc: str = '&', suggest_command: str = None, hover_text=None, open_url=None):
    """
    Returns the JSON rich text format from old formatted strings.
    Java Edition 1.13+ only.

    - `text`: The text to convert.
    - `esc`: The escape character. Can be anything, default is `&`.
    """

    # 10 years to get it right.
    output = []
    buffer = ""
    prop = properties.copy()
    i = 0
    for c in text:
        if c != esc:
            if text[i - 1] == esc and i > 0:
                if new_entry(prop, c):
                    prop["text"] = buffer
                    output.append(prop)
                    prop, buffer = properties.copy(), ""
                # 2nd gen gud algorithm (tm)
                try:
                    prop["color"] = color[c] if color.__contains__(c) else prop["color"]
                    prop[formatting[c] if formatting.__contains__(c) else 'None'] = True
                except KeyError:
                    pass
            else:
                buffer += c
        i += 1

    # Adds the final element to the list.
    prop["text"] = buffer
    output.append(prop)

    # Removes all false values.
    for i in range(len(output)):
        # Stack Overflow (tm)
        # https://stackoverflow.com/questions/29218750/what-is-the-best-way-to-remove-a-dictionary-item-by-value-in-python
        temp = {key: val for key, val in output[i].items() if (val is not False) or (val is None)}
        output[i] = temp
        output[i].pop("None")

    return output if len(output) > 1 else output[0]
