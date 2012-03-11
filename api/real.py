class PotentialReal:
    """Base class for potential real things"""
    def instance(self, *args, **kwargs):
        return self.inst(self, *args, **kwargs)

class Real:
    """Base class for a specific real thing in the game"""
    pass
