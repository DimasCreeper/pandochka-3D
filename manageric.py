# напиши здесь код создания и управления картой
from direct.showbase.ShowBase import ShowBase
import pickle
from random import*
class Mapmanager():
    def saveMap(self):
        blocks = self.land.getChildren()
        with open('lad.dat', 'wb') as fout:
            pickle.dump(len(blocks), fout)
            for block in blocks:
                x,y,z = block.getPos()
                pos = (int(x), int(y), int(z))
                pickle.dump('lad.dat', f)

    def loadMap(self):
        self.clear()
        with open('lad.dat', 'rb') as fout:
            lenght = pickle.load(fin)
            for i in range(lenght):
                pos = pickle.load(fin)
                self.addblock(pos)

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
    def delblockFrom(self, pos):
        x,y,z = pos
        pos = x, y, z
        blocks = self.findBlocks(pos)
        for block in blocks:
            block.removeNode()
    def build(self):
        angle = self.hero.getH() % 360
        pos = self.look_at(angle)
        if self.mode:
            self.land.addblock(pos)
        else:
            self.land.buildblock(pos)
    def destroy(self):
        angle = self.hero.getH() % 360
        pos = self.look_at(angle)
        if self.mode:
            self.land.delblock
        else:
            self.land.delblockFrom(pos)
    def buildblock(self, pos):
        x,y,z = pos
        new = self.findHighestEmpty(pos)
        if new[2] <= z + 1:
            self.addblock(new)
    def delblock(self,pos):
        blocks = self.findBlocks(pos)
        for block in blocks:
            block.removeNode()