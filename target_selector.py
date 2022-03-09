

class Target:
    def __init__(self):
        self.raw = ""

    def __str__(self):
        self.raw = self.raw[:-1]
        self.raw += "]" if len(self.raw) > 2 else ""
        return self.raw

    # Choosing range
    def nearest_player(self):
        if self.raw.__contains__("@"):
            raise SyntaxError("Cannot select two selector. Consider using limit().")
        self.raw = "@p"

    def all_players(self):
        if self.raw.__contains__("@"):
            raise SyntaxError("Cannot select two selector. Consider using limit().")
        self.raw = "@a["
        return self

    def all_entity(self):
        if self.raw.__contains__("@"):
            raise SyntaxError("Cannot select two selector. Consider using limit().")
        self.raw = "@e["
        return self

    def executor(self):
        if self.raw.__contains__("@"):
            raise SyntaxError("Cannot select two selector. Consider using limit().")
        self.raw = "@s"

    def random(self):
        if self.raw.__contains__("@"):
            raise SyntaxError("Cannot select two selector. Consider using limit().")
        self.raw = "@r["
        return self

    # Target selection criteria

    # By position

    def position(self, dimension: str, value: float, operator: str = "=", to=None):
        """
        Using individual coordinate value to search for target.
        """
        if ["x", "y", "z"].__contains__(dimension):
            raise SyntaxError(f"Invalid dimension: {dimension}. The only valid ones are x, y, and z.")

        self.raw += assemble_operator(dimension, operator, value, to)

        return self

    def distance(self, distance: float, operator: str = "="):
        """
        Select target using distance to the command executor.
        """
        if not distance >= 0:
            raise ValueError(f"Distance cannot be negative. Received {distance}")
        self.raw += f"distance{operator}{distance},"
        return self

    from . import commands

    def volume(self, v: commands.Volume):
        """
        Checks if target is in the specified.
        Must be equal.
        """
        self.raw += f"x={v.x},y={v.y},z={v.z},dx={v.dx},dy={v.dy},dz={v.dz},"
        return self

    # By limit

    def limit(self, sort_by: str, limit: int):
        """
        Checks if the entity is in the selected category.

        The sort_by can be:
         - near: default for @p. Sort from nearest to furthest.
         - far: the entity from the furthest to the nearest.
         - rand: choose random, like @r.
         - arb: by time created, default for @e and @a.
        """

        if not ["near", "far", "rand", "arb"].__contains__(sort_by):
            raise SyntaxError(f"Invalid sorting option. Must be near, far, rand, or arb. Received {sort_by}")
        if limit is None or limit <= 0:
            raise ValueError(f"Invalid entity selecting limit. Must be ≥ 0. Received {limit}")

        self.raw += f"limit={limit},sort={sort_by},"

        return self

    # Scoreboard hell.

    def tag(self, tag_name: str, operator: str = None):
        if not ["=", "!=", None].__contains__(operator):
            raise SyntaxError(f"Illegal operator: {operator}. Expected =, != or False (no tag), True (has at least one tag)")
        if ["=", "!="].__contains__(operator) and not type(tag_name) == bool:
            self.raw += f"tag{operator}{tag_name},"
        elif tag_name:
            self.raw += "tag=!,"
        else:
            self.raw += "tag=,"

        return self

    def team(self, team_name: str, operator: str = None):
        if not ["=", "!=", None].__contains__(operator):
            raise SyntaxError(
                f"Illegal operator: {operator}. Expected =, != or False (no team), True (has at least one team)")
        if ["=", "!="].__contains__(operator) and not type(team_name) == bool:
            self.raw += f"team{operator}{team_name},"
        elif team_name:
            self.raw += "team=!,"
        else:
            self.raw += "team=,"

        return self

    # By traits

    def name(self, name: str, operator: str = "="):
        """
        If the entity has the same name or not.
        """
        if not ["=", "!="].__contains__(operator):
            raise SyntaxError(f"Illegal operator: {operator}. Expected = or !=")
        self.raw += f"name{operator}{name},"
        return self

    def level(self, value: float, operator: str = "="):
        """
        Experience stuff
        """
        self.raw += assemble_operator("level", operator, value)
        return self

    def gamemode(self, gamemode: str, operator: str = "="):
        """
        If the target has or doesn't have gamemode.

        Creative: creative, c, 1
        Survival: survival, s, 0
        Adventure: adventure, a, 2
        """

        def abb():
            if ["c", "1", "creative"].__contains__(gamemode):
                return "creative"
            if ["s", "0", "survival"].__contains__(gamemode):
                return "survival"
            if ["a", "2", "adventure"].__contains__(gamemode):
                return "adventure"

        if not ["=", "!="].__contains__(operator):
            raise SyntaxError(f"Illegal operator: {operator}. Expected = or !=")
        if not ["c", "creative", "1", "s", "survival", "a", "adventure"]:
            raise SyntaxError("Invalid gamemode.")
        self.raw += f"gamemode{operator}{abb()},"

        return self


def assemble_operator(op: str, operator: str, value, to: int = None):
    output = ""
    if value is None:
        raise SyntaxError(f"Value must not be None.")
    if ["=", "!="].__contains__(operator):
        output += f"{op}{operator}{value},"
    elif [">", "!>"].__contains__(operator):
        output += f"{op}={value}..," if operator == "<" else f"{op}!={value}..,"
    elif ["!<", "<"].__contains__(operator):
        output += f"{op}=..{value}," if operator == "<" else f"{op}!=..{value},"
    elif ["!-", "-"].__contains__(operator):
        if to is None:
            raise SyntaxError(f"The to argument cannot be None when using the range operator (-).")
        output += f"{op}={value}..{to}," if operator == "-" else f"{op}!={value}..{to},"
    else:
        raise SyntaxError(f"Operator must be: <, >, -, =, !<, !>, !=, !-. Received {operator}")

    return output
