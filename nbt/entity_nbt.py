from ..abc import Item, Position, UUID, JSONText, Entity
from .attributes import EntityAttribute
from ..utils import asm_item


class EntityNBT:
    """
    The NBT of an entity
    """

    def __init__(self):
        self.raw = ""
        self.attributes = []

    def __str__(self):
        return "{" + self.raw[:-1] + "}"

    def motion(self, value_x: float = 0.0, value_y: float = 0.0, value_z: float = 0.0):
        """
        The motion of the entity.
        """
        self.raw += f"Motion:[{value_x},{value_y},{value_z}],"
        return self

    def rotate(self, yaw: float = 0.0, pitch: float = 0.0):
        """
        The rotation of the entity.
        """
        self.raw += f"Rotation:[{yaw}F,{pitch}F],"
        return self

    def burn_time_left(self, ticks: int):
        """
        The time left that the entity burn until the fire distinguish itself.
        """
        self.raw += f"Fire:{ticks},"
        return self

    def has_visual_fire(self, option: bool = True):
        """
        Whether the entity has fire visually on it or not.
        """
        self.raw += f"HasVisualFire:{'1b' if option else '0b'},"
        return self

    def air_left(self, ticks: int):
        """
        The air of the entity left underwater.
        """
        self.raw += f"Air:{ticks},"
        return self

    def on_ground(self, option: bool = True):
        """
        Whether the entity is on ground or not.
        """
        self.raw += f"OnGround:{'1b' if option else '0b'},"
        return self

    def no_gravity(self, option: bool = True):
        """
        Whether the entity has gravity or not.
        """
        self.raw += f"NoGravity:{'1b' if option else '0b'},"
        return self

    def invulnerable(self, option: bool = True):
        """
        Whether the entity is attackable for player in survival mode.
        """
        self.raw += f"Invulnerable:{'1b' if option else '0b'},"
        return self

    def silent(self, option: bool = True):
        """
        Whether the entity makes noise.
        """
        self.raw += f"Silent:{'1b' if option else '0b'},"
        return self

    def glowing(self, option: bool = True):
        """
        Whether the entity is glowing.
        """
        self.raw += f"Glowing:{'1b' if option else '0b'},"
        return self

    def name(self, name: JSONText | list[JSONText]):
        """
        Sets the name of the entity.
        """
        self.raw += f"CustomName:'{name}',"
        return self

    def tag(self, *args: str):
        """
        Custom tag name for the target selector.
        """
        self.raw += f"Tags:[{','.join(args)}],"
        return self

    def fall_distance(self, distance: float):
        """
        The distance the entity has fallen. Affects fall damage.
        """
        self.raw += f"FallDistance:{distance}f,"
        return self

    def portal_cooldown(self, ticks: int):
        """
        The time the entity has left the portal from now
        """
        self.raw += f"PortalCooldown:{ticks},"
        return self

    # def uuid(self, uuid: str):
    #     """
    #     Set the UUID of the entity. Two entities with the same UUID cannot
    #     exist at the same time.
    #
    #     UUID here consists of 36 hex digits, representing a 128-bit number.
    #     """
    #     nuuid = uuid.replace("-", "")
    #     # c7562635-dee1-47e6-8c6f-3c4a7b9da042
    #     if len(nuuid) != 36:
    #         raise SyntaxError("UUID can only consist of 36 hex digits.")
    #     self.raw += f"UUID:[I;{nuuid[:8]},{nuuid[8:12]},{nuuid[12:16]}]"

    def hurt_time(self, ticks: int):
        """
        The amount of time the entity flashes red when attacked.
        """
        self.raw += f"HurtTime:{ticks},"
        return self

    def death_time(self, ticks: int):
        """
        The amount of time that the mob has been dying. Controls death animation.
        """
        self.raw += f"DeathTime:{ticks},"
        return self

    def loot_table_path(self, path: str):
        """
        The file path to the loot table for that entity.
        """
        # Somehow Minecraft requires you to double escape
        path.replace("\\", "\\\\")
        self.raw += f"DeathLootTable:\"{path}\","
        return self

    def left_handed(self, option: bool = True):
        """
        Whether the entity's main hand is the left hand.
        Only affects human-like entities like Zombies and Skeletons.
        """
        self.raw += f"LeftHanded:{'1b' if option else '0b'},"
        return self

    def team(self, team_name: str):
        """
        Makes the entity instantly joins the team with
        the name specified when spawned.
        """
        self.raw += f"Team:\"{team_name}\","
        return self

    def leash(self, to: Position | UUID):
        """
        What is the entity leashed to, or whether it is leashed.
        """
        if type(to) == UUID:
            result = f"UUID:{to}"
        elif type(to) == Position:
            result = f"X:{to.x},Y:{to.y},Z:{to.z}"
        else:
            raise SyntaxError("The entity can only be leashed to a Position or an UUID of an entity.")

        result = "{" + result + "}"
        self.raw += f"Leashed:1b,Leash:{result},"
        return self

    def enable_despawn(self, option: bool = True):
        """
        Whether the entity will despawn
        """
        self.raw += f"PersistenceRequired:{'1b' if option else '0b'},"
        return self

    def disable_ai(self, option: bool = True):
        """
        Whether the entity will attempt to move.
        """
        self.raw += f"NoAI:{'1b' if option else '0b'},"
        return self

    def pick_up_item(self, option: bool = True):
        """
        Whether the entity can pick up items and wear armour
        it picked up them.
        """
        self.raw += f"CanPickUpLoot:{'1b' if option else '0b'},"
        return self

    def wielding(
            self,
            main_hand: Item = None,
            off_hand: Item = None,
            head: Item = None,
            body: Item = None,
            leggings: Item = None,
            boots: Item = None
    ):
        """
        Set the item that the entity is wielding or wearing.
        """
        # != is xor.
        # https://stackoverflow.com/questions/432842/how-do-you-get-the-logical-xor-of-two-variables-in-python
        if (main_hand is None) != (off_hand is None):
            self.raw += "HandItems:["
            self.raw = self.raw + asm_item(main_hand) + ","
            self.raw = self.raw + asm_item(off_hand)
            self.raw += "],"
        if ((head is None) != (body is None)) != ((leggings is None) != (boots is None)):
            self.raw += "ArmorItems:["
            self.raw = self.raw + asm_item(boots) + ","
            self.raw = self.raw + asm_item(leggings) + ","
            self.raw = self.raw + asm_item(body) + ","
            self.raw = self.raw + asm_item(head)
            self.raw += "],"
        return self

    def absorption(self, amount: float):
        """
        The amount of health gained by absorption effect, like
        eating a golden apple.
        """
        self.raw += f"AbsorptionAmount:{amount}f,"
        return self

    def health(self, amount: float):
        """
        The amount of base HP the entity gets.
        """
        self.raw += f"Health:{amount}f,"
        return self

    def sleeping_at(self, at: Position):
        """
        Sets the block that is the top of a bed (with the pillow)
        that the entity sleeps on when spawned.
        """
        self.raw += f"SleepingX:{at.x},SleepingY:{at.y},SleepingZ:{at.z},"
        return self

    def set_attributes(self, attribute: EntityAttribute):
        self.raw = self.raw + str(attribute) + ","

    def in_love(self, ticks: int):
        """
        The time left for the entity to search for a mate.
        """
        self.raw += f"InLove:{ticks},"
        return self

    def age(self, ticks: int):
        """
        The age of the entity.
        Negative values are considered a baby.
        Zero or above is considered an adult.
        Larger than zero is the time left until the entity can be bred again.
        """
        self.raw += f"Age:{ticks},"
        return self

    def forced_age(self, ticks: int):
        """
        A value of age which will be assigned to this mob when it grows up.
        Incremented when a baby mob is fed.
        """
        self.raw += f"ForcedAge:{ticks},"
        return self

    def love_cause(self, cause: UUID):
        """
        The cause of the entity's breading.
        """
        self.raw += f"LoveCause:{cause},"
        return self

    def passengers(self, *entities: Entity):
        """
        Sets the passengers of the entity.
        Can be chained indefinitely.
        """
        self.raw += "Passengers:["
        for i in entities:
            self.raw = self.raw + "{" + f"id:{i.type},{i.nbt}" + "},"
        self.raw = self.raw[:-1] + "],"
        return self
