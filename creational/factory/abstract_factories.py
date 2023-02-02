"""from Eckel B.
Character object interacts with Obstacle object, but there are different types of Characters and obstacles depending
on what kind of game you are playing.
You determine the kind of game by choosing a praticular GameElementFactory and then GameEnviroment controls
the setup and play of the game.
"""
class Obstacle:
    def action(self): pass

class Character:
    def interactWith(self, obstacle): pass

# caracters implement InteractWith obstacle method
class Kitty(Character):
    def interactWith(self, obstacle):
        print("Kitty has encountered a", obstacle.action())

class KungFuGuy(Character):
    def interactWith(self,obstacle):
        print("KungFuGuy has encountered a", obstacle.action())

class Puzzle(Obstacle):
    def action(self):
        print("Puzzle")

class NastaWeapon(Obstacle):
    def action(self):
        print("NastyWeapon")


class GameElementFactory:
    def makeCharacter(self): pass
    def makeObstacle(self): pass

# different games
class KittensAndPuzzle(GameElementFactory):
    def makeCharacter(self): return Kitty()
    def makeObstacle(self): return Puzzle()

class KillAndDismember(GameElementFactory):
    def makeCharacter(self): return KungFuGuy()
    def makeObstacle(self): return NastaWeapon()

class GameEnviroment:
    def __init__(self, factory):
        self.factory = factory
        self.p = factory.makeCharacter()
        self.ob = factory.makeObstacle()

    def play(self):
        self.p.interactWith(self.ob)

g1 = GameEnviroment(KittensAndPuzzle())
g2 = GameEnviroment(KillAndDismember())
g1.play()
g2.play()
