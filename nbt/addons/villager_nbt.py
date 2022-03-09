from enum import Enum
from ..entity_nbt import EntityNBT
from .. import Item, Position, UUID


class GossipType(Enum):
    """
    Represents the type of gossip.
    """

    MAJOR_POSITIVE = "major_positive"
    MAJOR_NEGATIVE = "major_negative"
    MINOR_POSITIVE = "minor_positive"
    MINOR_NEGATIVE = "minor_negative"
    TRADING = "trading"
    GOLEM = "golem"


class Gossip:
    """
    Represents a villager's gossip.
    """

    def __init__(self, gossip_type: GossipType, value: int, target: UUID):
        self.type = gossip_type
        self.value = value
        self.target = target

    def __str__(self):
        return "{" + f"Type:\"{self.type}\",Value:{self.value},Target:{self.target}" + "}"


class Trade:
    """
    Represents a trade of a villager.
    """

    def __init__(
            self,
            buy: Item,
            sell: Item,
            buy2: Item = None,
            reward_exp: bool = True,
            max_uses: int = None,
            uses: int = None,
            xp: int = None,
            price_multiplier: int = None,
            special_price: int = None,
            demand: int = None,
    ):
        """
        Initializes a new Trade.

        Parameters
        ----------
        buy : Item
            The item the villager wants
        buy2: Item
            The second item the villager wants. Optional.
        sell : Item
            The item the villager sells.
        reward_exp : bool
            Whether the villager should reward experience for this trade. Optional.
        max_uses : int
            The maximum number of times the villager can trade this trade. Optional.
        uses : int
            The number of times the villager has traded this trade. Optional.
        xp : int
            The amount of experience the villager should reward. Optional.
        price_multiplier : int
            The price multiplier of the trade. Optional.
        special_price : int
            A price modifier on the original prices. Optional.
        demand : int
            The demand of the trade. Prices is calculated accordingly. Optional.
        """
        self.buy = buy
        self.buy2 = buy2
        self.sell = sell
        self.reward_exp = reward_exp
        self.max_uses = max_uses
        self.uses = uses
        self.xp = xp
        self.price_multiplier = price_multiplier
        self.special_price = special_price
        self.demand = demand

    def __str__(self):
        output = "{"
        output += f"rewardExp:{'1b' if self.reward_exp else '0b'},"
        output += f"maxUses:{self.max_uses}," if self.max_uses is not None else ""
        output += f"uses:{self.uses}," if self.uses is not None else ""
        output += f"xp:{self.xp}," if self.xp is not None else ""
        output += f"priceMultiplier:{self.price_multiplier}," if self.price_multiplier is not None else ""
        output += f"specialPrice:{self.special_price}," if self.special_price is not None else ""
        output += f"demand:{self.demand}," if self.demand is not None else ""
        output = output + "buy:{" + f"id:\"{self.buy.name}\",Count:{self.buy.amount}b,tag:{self.buy.nbt}" + "},"
        if self.buy2 is not None:
            output = output + "buyB:{" + f"id:\"{self.buy2.name}\",Count:{self.buy2.amount}b,tag:{self.buy2.nbt},"
        output = output + "sell:{" + f"id:\"{self.sell.name}\",Count:{self.sell.amount}b,tag:{self.sell.nbt}" + "}"
        output = output + "}"
        return output


class Profession(Enum):
    """
    Profession for the villager.
    """
    ARMORER = "minecraft:armorer"
    BUTCHER = "minecraft:butcher"
    CARTOGRAPHER = "minecraft:cartographer"
    CLERIC = "minecraft:cleric"
    FARMER = "minecraft:farmer"
    FISHERMAN = "minecraft:fisherman"
    FLETCHER = "minecraft:fletcher"
    LEATHER_WORKER = "minecraft:leatherworker"
    LIBRARIAN = "minecraft:librarian"
    MASON = "minecraft:mason"
    NITWIT = "minecraft:nitwit"
    SHEPHERD = "minecraft:shepherd"
    TOOL_SMITH = "minecraft:toolsmith"
    WEAPON_SMITH = "minecraft:weaponsmith"


class VillagerType(Enum):
    """
    The type of villager. (What they look like)
    """
    DESERT = "minecraft:desert"
    SNOW = "minecraft:snow"
    SAVANNA = "minecraft:savanna"
    PLAINS = "minecraft:plains"
    TAIGA = "minecraft:taiga"
    SWAMP = "minecraft:swamp"


class VillagerNBT(EntityNBT):
    """
    NBT for a villager.
    """

    def __init__(self):
        super().__init__()
        self.villager_data = "VillagerData:"

    def profession(self, profession):
        """
        Set the profession for the villager.
        """
        self.villager_data += f"profession:{profession},"
        return self

    def type(self, villager_type: VillagerType):
        """
        Set the type of villager.
        """
        self.villager_data += f"type:{villager_type},"
        return self

    def level(self, level: int):
        """
        Sets the level of the villager.
        Set it to 99 to hide the level bar.
        """
        self.villager_data += f"level:{level},"
        return self

    def willing_to_mate(self, option: bool = True):
        """
        Whether the villager wants to mate.
        """
        self.villager_data += f"Willing:{'1b' if option else '0b'},"
        return self

    def last_restock(self, tick: int):
        """
        The last time the villager restocked.
        """
        self.villager_data += f"LastRestock:{tick},"
        return self

    def xp(self, amount: int):
        """
        The amount of XP the villager has.
        """
        self.villager_data += f"Xp:{amount},"
        return self

    def trade(self, *trades: Trade):
        """
        Add trades the villager.
        """
        if trades is None:
            self.raw += "Offers:{},"
            return self
        self.raw += "Offers:{Recipes:["
        for i in trades:
            self.raw += str(i) + ","
        self.raw = self.raw[:-1] + "]},"
        return self

    def memory(self, meeting_point: Position = None, home: Position = None, job_site: Position = None):
        """
        Sets the places that the villager goes day by day.
        """
        if meeting_point is None and home is None and job_site is None:
            return self

        self.raw += "Brain:{memories:{"
        if meeting_point is not None:
            self.raw += "\"minecraft:meeting_point\":{value:{pos:"
            self.raw += f"[I;{meeting_point.x},{meeting_point.y},{meeting_point.z}]," \
                        f"dimension:\"{meeting_point.dimension}\""
            self.raw += "}},"
        if home is not None:
            self.raw += "\"minecraft:home\":{value:{pos:"
            self.raw += f"[I;{home.x},{home.y},{home.z}]," \
                        f"dimension:\"{home.dimension}\""
            self.raw += "}},"
        if job_site is not None:
            self.raw += "\"minecraft:job_site\":{value:{pos:"
            self.raw += f"[I;{job_site.x},{job_site.y},{job_site.z}]," \
                        f"dimension:\"{job_site.dimension}\""
            self.raw += "}},"
        self.raw = self.raw[:-1] + "}},"
        return self

    def gossip(self, *gossip: Gossip):
        """
        Sets the gossip for the villager.
        """
        self.raw += "Gossip:["
        for i in gossip:
            self.raw += str(i) + ","
        self.raw = self.raw[:-1] + "],"
        return self

    def inventory(self, *items: Item):
        """
        The items in the inventory of the villager.
        Villagers only has 8 inventory slots. If you add more, and it will be removed automatically.
        If you duplicate an item it will be stacked.
        """
        self.raw += "Inventory:["
        for i in items:
            self.raw = self.raw + "{" + f"id:{i.name},Count:{i.amount}b,tag:" + "{" + f"{i.nbt}," + "},"
        self.raw = self.raw[:-1] + "],"
        return self
