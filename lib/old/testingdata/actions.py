from random import randint, choice
from api.action import Action


def exec_from_dict(d):
    def exec_(self):
        for change in d.items():
            for target in self.targets:
                target.stats[change[0]] -= change[1]
    return exec_

poke = Action('poke', {"exec":execmaker(1)})
hit = Action('hit', {"exec":execmaker(2)})

dmg_rules = {"melee":"self.actor.stats['STR']+\
randint(self.actor.stats['MINWPNDMG'], self.actor.stats['MAXWPNDMG'])-\
target.stats['DEF']*self.metadata['change']",
"magic":"(self.actor.stats['INT']*\
randint(self.actor.stats['MINWPNDMG'], self.actor.stats['MAXWPNDMG'])-\
target.stats['MDEF'])*self.metadata['change']"}

def simple_exec(self):
    if "extra" in self.metadata:
        extra = self.metadata["extra"].copy(self.battle)
        extra.complete(self.actor, self.targets)
        self.battle.timeline.addaction(extra, self.metadata["extra"].metadata['delay'])
    for target in self.targets:
        dmg = eval(self.dmg)
        self.metadata['dmg'][target] = dmg
        print(target.name, "lost", dmg, "health!")

def simpleinit(self):
    self.dmg = dmg_rules[self.metadata["type"]]
    self.metadata['dmg'] = {}
    self.actor.stats['MP'] -= self.metadata["MPcost"]

def special_exec(self):
    self.actor.stats['MP'] -= self.metadata["MPcost"]
    n = 30
    self.actor.stats["HP"] += n
    self.metadata['dmg'][self.actor] = (-n)
    print(self.actor.name, "has gained", n, "HP")

def boom(self):
    print("Boom!")
    for player in self.targets:
        dodge = player.stats['Dodge']
        dodge = int(randint(0, 1000)<dodge)
        if dodge:
            dmg = 0
            print(player.name, "dodged the bomb!")
        else:
            dmg = randint(0, 100)*self.actor.stats['INT']
            player.stats["HP"]-=dmg
            print(player.name, "lost ", dmg, "sanity in the blast!")
        self.metadata["dmg"][player] = dmg

    self.actor.actions = [action for action in self.actor.actions if action.name != self.name]
    bomb = self.actor.belongs["Bomb"]
    self.actor.rmbelong(bomb)
    del self.actor.belongs["Bomb"]

def poisoned(self):
    if self.copy_status < 2:
        self.dmg = self.actor.stats["INT"] + self.actor.stats["STR"]
    print(self.targets[0].name, "took", self.dmg, "damadge from poison")
    self.targets[0].stats["HP"]-=self.dmg
    if self.dmg > 1:
        newpoison = self.copy(self.battle)
        newpoison.complete(self.actor, self.targets)
        newpoison.dmg = self.dmg-1
        self.battle.timeline.addaction(newpoison, 1)


