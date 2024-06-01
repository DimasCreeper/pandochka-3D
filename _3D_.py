#3D Game
from direct.actor.Actor import Actor
from random import*
from manageric import Mapmanager
from direct.showbase.ShowBase import ShowBase
from math import pi, sin, cos
from direct.task import Task
from panda3d.core import Point3
from direct.interval.IntervalGlobal import Sequence
from direct.gui.DirectGui import *
from direct.task.Timer import Timer
from direct.showbase import Audio3DManager
from heroo import hero
from direct.gui.OnscreenText import OnscreenText


class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.land = Mapmanager()
        self.land.loadLand('lad.txt')
        self.hero = hero((25,25,200),self.land)
        base.setBackgroundColor(random(),random(),random(),1)
        mytimer = DirectLabel()
        mytimer.reparentTo(render)
        mytimer.setScale(8)
        mytimer.setZ(99)
        mytimer.setColor(random(),random(),random(),1)
        #mytimer.setZ(-99)
        def timerTask(task):
            secondsTime = int(task.time)
            minutesTime = int(secondsTime/60)
            hoursTime = int(minutesTime/60)
            mytimer['text'] = "%02d:%02d:%02d" % (hoursTime, minutesTime%60, secondsTime%60)
            return Task.cont
        taskMgr.add(timerTask, 'timerTask')
        base.setFrameRateMeter(True)
        textObject = OnscreenText(text='Your task is reach the top of the skyscraper!', pos=(-0.7, 0.9), scale=0.05)
        frameTime = globalClock.getFrameTime()
        self.model = loader.loadModel("models/environment")
        self.model.reparentTo(render)
        self.model2 = loader.loadModel('Sailboat.egg')
        self.model4 = loader.loadModel('Fighter.egg')
        self.mod = loader.loadModel('Smiley')
        self.mod.reparentTo(render)
        self.mod.setScale(7)
        self.model4.reparentTo(render)
        self.model2.reparentTo(render)
        self.mod.setPos(29, 85, 25)
        self.model.setPos(2, 25, 3)
        self.model2.setPos(55, 33, 10)
        self.model4.setPos(55, -85, 120)
        self.model.setScale(1)
        self.model4.setScale(2)
        self.model2.setScale(2)
        base.camLens.setFov(120)
        self.pandaActor = Actor("models/panda-model",
                            {"walk": "models/panda-walk4"})
        self.pandaActor.setScale(0.05, 0.05, 0.05)
        self.pandaActor.reparentTo(self.render)
        # Loop its animation.
        self.pandaActor.loop("walk")
        posInterval1 = self.pandaActor.posInterval(13,
                                                   Point3(-15, -90, 0),
                                                   startPos=Point3(-15, 90, 0))
        posInterval2 = self.pandaActor.posInterval(13,
                                                   Point3(-15, 90, 0),
                                                   startPos=Point3(-15, -90, 0))
        hprInterval1 = self.pandaActor.hprInterval(3,
                                                   Point3(180, 0, 0),
                                                   startHpr=Point3(0, 0, 0))
        hprInterval2 = self.pandaActor.hprInterval(3,
                                                   Point3(0, 0, 0),
                                                   startHpr=Point3(180, 0, 0))

        # Create and play the sequence that coordinates the intervals.
        self.pandaPace = Sequence(posInterval1, hprInterval1,
                                  posInterval2, hprInterval2,
                                  name="pandaPace")
        self.pandaPace.loop()
        self.ship = Actor("Fighter.egg",
        {"walk": "Fighter-walk.egg"})
        self.ship.setScale(1, 1, 1)
        self.ship.reparentTo(self.render)
        # Loop its animation.
        self.ship.loop("run")
        posInterval1 = self.ship.posInterval(2,
                                                Point3(0, -90, 60),
                                                startPos=Point3(0, 90, 60))
        posInterval2 = self.ship.posInterval(2,
                                                Point3(0, 90, 60),
                                                startPos=Point3(0, -90, 60))
        hprInterval1 = self.ship.hprInterval(2,
                                                Point3(180, 0, 0),
                                                startHpr=Point3(0, 0, 0))
        hprInterval2 = self.ship.hprInterval(2,
                                                Point3(0, 0, 0),
                                                startHpr=Point3(180, 0, 0))
        self.shipPace = Sequence(posInterval1, hprInterval1,
                                posInterval2, hprInterval2,
                                name="shipPace")
        self.shipPace.loop()
        self.ship_ = Actor("Fighter.egg",
        {"walk": "Fighter-walk.egg"})
        self.ship_.setScale(1, 1, 1)
        self.ship_.reparentTo(self.render)
        # Loop its animation.
        self.ship_.loop("run")
        posInterval1 = self.ship_.posInterval(2,
                                                Point3(1110, -90, 60),
                                                startPos=Point3(1000, 1800, 2000))
        posInterval2 = self.ship_.posInterval(2,
                                                Point3(330, 90, 60),
                                                startPos=Point3(1000, -1800, 2000))
        hprInterval1 = self.ship_.hprInterval(2,
                                                Point3(180, 770, 2230),
                                                startHpr=Point3(330, 230, 220))
        hprInterval2 = self.ship_.hprInterval(2,
                                                Point3(206, 440, 223),
                                                startHpr=Point3(180, 0, 0))
        self.shipPace_ = Sequence(posInterval1, hprInterval1,
                                posInterval2, hprInterval2,
                                name="shipPace")
        self.shipPace_.loop()
        self.blimp = Actor("Blimp.egg",
        {"walk": "Blimp.egg"})
        self.blimp.setScale(7, 7, 7)
        self.blimp.reparentTo(self.render)
        # Loop its animation.
        self.blimp.loop("run")
        posInterval1 = self.blimp.posInterval(3,
                                                Point3(3000, -1800, 2000),
                                                startPos=Point3(3000, 1800, 2000))
        posInterval2 = self.blimp.posInterval(3,
                                                Point3(3000, 1800, 2000),
                                                startPos=Point3(3000, -1800, 2000))
        hprInterval1 = self.blimp.hprInterval(3,
                                                Point3(180, 0, 0),
                                                startHpr=Point3(330, 0, 0))
        hprInterval2 = self.blimp.hprInterval(3,
                                                Point3(0, 0, 0),
                                                startHpr=Point3(180, 0, 0))
        self.blimpPace = Sequence(posInterval1, hprInterval1,
                                posInterval2, hprInterval2,
                                name="blimpPace")
        self.blimpPace.loop()
        self.blimp2 = Actor("Blimp.egg",
        {"walk": "Blimp.egg"})
        self.blimp2.setScale(12, 12, 12)
        self.blimp2.reparentTo(self.render)
        # Loop its animation.
        self.blimp2.loop("run")
        posInterval1 = self.blimp2.posInterval(3,
                                                Point3(0, -1800, 2000),
                                                startPos=Point3(0, 1800, 2000))
        posInterval2 = self.blimp2.posInterval(3,
                                                Point3(0, 1800, 2000),
                                                startPos=Point3(0, -1800, 2000))
        hprInterval1 = self.blimp2.hprInterval(3,
                                                Point3(180, 0, 0),
                                                startHpr=Point3(0, 0, 0))
        hprInterval2 = self.blimp2.hprInterval(3,
                                                Point3(0, 0, 0),
                                                startHpr=Point3(180, 0, 0))
        self.blimp2Pace = Sequence(posInterval1, hprInterval1,
                                posInterval2, hprInterval2,
                                name="blimp2Pace")
        self.blimp2Pace.loop()
game = Game()
game.run()