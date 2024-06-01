# напиши здесь код основного окна игры
from direct.showbase.ShowBase import ShowBase
from mapmanager import Mapmanager
from random import*
from hero import hero
class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        base.setBackgroundColor(random(),random(),random(),1)
        base.setFrameRateMeter(True)
        self.land = Mapmanager()
        x,y = self.land.loadLand('land.txt')
        self.hero = hero((x//2,y//2,2),self.land)
        base.camLens.setFov(90)

game = Game()
game.run()
