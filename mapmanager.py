# напиши здесь код создания и управления картой
from direct.showbase.ShowBase import ShowBase
from random import*
class Mapmanager():
    def __init__(self):
        self.texture = 'block.png'
        self.model = 'block.egg'
        self.colors = [(random(),random(),random(),1),
                        (random(),random(),random(),1),
                        (random(),random(),random(),1)]
        self.startnew()
        self.addblock((0,10,0))

    def addblock(self, pos):
        self.block = loader.loadModel(self.model)
        self.block.setTexture(loader.loadTexture(self.texture))
        self.block.setPos(pos)
        self.color = self.getColor(pos[2])
        self.block.setColor(self.color)
        self.block.reparentTo(self.land)
        self.block.setTag('at', str(pos))


    def startnew(self):
        self.land = render.attachNewNode('Land')

    def isEmpty(self,pos):
        blocks = self.findBlocks(pos)
        if blocks:
            return False
        else:
            return True
    def findBlocks(self,pos):
        pass

    def findHighestEmpty(self,pos):
        x,y,z = pos
        z = 1
        while not self.isEmpty((x,y,z)):
            z += 1
        return (x,y,z)

    def findBlocks(self,pos):
        return self.land.findAllMatches('=at=' + str(pos))

    def clear(self):
        self.land.removeNode()
        self.startnew()

    def getColor(self, z):
        if z < len(self.colors):
            return self.colors[z]
        else:
            return self.colors[len(self.colors)-1]

    def loadLand(self, filename):
        self.clear()
        with open(filename) as file:
            y = 0
            for line in file:
                x = 0
                line = line.split(' ')
                for z in line:
                    for z0 in range(int(z)+1):
                        block = self.addblock((x, y, z0))
                    x += 1
                y += 1
        return x, y   


