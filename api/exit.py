class Exit:
    def __init__(self, condition, effect = lambda player, players:None):
        self.condition = condition
        self.effect = effect
