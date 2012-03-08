from api import Status


@Status
def poison(self):
    being = self.being
    print(being.name, "took", self.poison, "damage from poison")
    being.stats["HP"] -= self.poison
    self.poison -= 1
    if self.poison < 1:
        being.status_list.remove(self)
