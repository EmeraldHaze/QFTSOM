class Exit:
    """This represents a possible way to get out of a battle, and the
    consqeuances of doing so. Has a condition function that should return
    weather the given player exited or not, and an effect function"""
    def __init__(self, condition, effect=lambda player, players: None):
        self.condition = condition
        self.effect = effect
