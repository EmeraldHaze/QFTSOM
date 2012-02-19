from api import Status

@Status
def poison(self):
    being = self.being
    print(being.name, "took", being.data['poison'], "damadge from poison")
    being.stats["HP"] -= being.data['poison']
    being.data['poison'] -= 1
    if being.data['poison'] < 1:
        being.status_list.remove(self)
