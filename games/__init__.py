from core import config

if config.choosen_game.isalpha():
    exec("from games." + config.choosen_game + " import game as choosen_game")
else:
    raise Exception("Nonalphabetical choosen game name - code injection?")
