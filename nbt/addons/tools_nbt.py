from ..item_nbt import NBT


class ToolNBT(NBT):
    """
    The NBT for a tool.
    """

    def __init__(self):
        super().__init__()

    def damage(self, amount: float):
        self.raw += f"Damage:{amount},"

    def repair_cost(self, level: int):
        self.raw += f"RepairCost:{level},"
