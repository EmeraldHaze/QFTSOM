from api import Status
@Status
def poison(self):
    player = self.player
    print(player.name, "took", player.data['poison'], "damadge from poison")
    player.stats["HP"] -= player.data['poison']
    player.data['poison'] -= 1
    if player.data['poison'] < 1:
        player.status_list.remove(self)