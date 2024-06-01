# напиши свой код здесь
class hero():
    def __init__(self, pos, land):
        self.mode = True
        self.land = land
        self.hero = loader.loadModel('smiley')
        self.hero.setColor(5,4,0)
        self.hero.setScale(0.5)
        self.hero.setPos(pos)
        self.hero.reparentTo(render)
        self.camersBind()
        self.accept_events()
    def camersBind(self):
        base.disableMouse()
        base.camera.reparentTo(self.hero)
        base.camera.setH(180)
        base.camera.setPos(0,0,1.5)
        self.cameraOn = True
    def cameraUp(self):
        pos = self.hero.getPos()
        base.mouseInterfaceNode.setPos(-pos[0], -pos[1], -pos[2] - 3 )
        base.camera.reparentTo(render)
        base.enableMouse()
        self.cameraOn = False
    def accept_events(self):
        base.accept('z', self.changeMode)
        base.accept('q', self.build)
        #base.accept('p', self.saveMap)
        #base.accept('i', self.loadMap)
        base.accept('e', self.destroy)
        base.accept('q'+'-repeat', self.build)
        base.accept('e'+'-repeat', self.destroy)
        base.accept('b', self.changeView)
        base.accept('s', self.back)
        base.accept('s'+'-repeat', self.back)
        base.accept('o', self.up)
        base.accept('o'+'-repeat', self.up)
        base.accept('l', self.down)
        base.accept('l'+'-repeat', self.down)
        base.accept('w', self.forward)
        base.accept('w'+'-repeat', self.forward)
        base.accept('d', self.right)
        base.accept('d'+'-repeat', self.right)
        base.accept('a', self.left)
        base.accept('a'+'-repeat', self.left)
        base.accept('n', self.turn_left)
        base.accept('n'+'-repeat', self.turn_left)
        base.accept('m', self.turn_right)
        base.accept('m'+'-repeat', self.turn_right)
    def changeMode(self):
        if self.mode == True:
            self.mode = False
        else:
            self.mode = True
    def changeView(self):
        if self.cameraOn == True:
            self.cameraUp()
        elif self.cameraOn == False:
            self.camersBind()
    def up(self):
        self.hero.setZ(self.hero.getZ()+1)
    def down(self):
        self.hero.setZ(self.hero.getZ()-1)
    def turn_left(self):
        self.hero.setH((self.hero.getH() + 5) % 360)
    def turn_right(self):
        self.hero.setH((self.hero.getH() - 5) % 360)
    def back(self):
        angle =(self.hero.getH()+180) % 360
        self.move_to(angle)
    def forward(self):
        angle =(self.hero.getH()) % 360
        self.move_to(angle)
    def left(self):
        angle = (self.hero.getH()+90) % 360
        self.move_to(angle)
    def right(self):
        angle = (self.hero.getH()+270) % 360
        self.move_to(angle)
    def just_move(self, angle):
        pos = self.look_at(angle)
        self.hero.setPos(pos)
    def look_at(self, angle):
        from_x = round(self.hero.getX())
        from_y = round(self.hero.getY())
        from_z = round(self.hero.getZ())
        dx, dy = self.check_dir(angle)
        return from_x + dx,from_y + dy, from_z
    def check_dir(self, angle):
        if angle >= 0 and angle <= 20:
            return 0, -1
        if angle >= 0 and angle <= 65:
            return 1, -1
        if angle >= 0 and angle <= 110:
            return 1, 0
        if angle >= 0 and angle <= 155:
            return 1, 1
        if angle >= 0 and angle <= 200:
            return 0, 1
        if angle >= 0 and angle <= 245:
            return -1, 1
        if angle >= 0 and angle <= 290:
            return -1, 0
        if angle >= 0 and angle <= 355:
            return -1, -1
        if angle >= 0 and angle <= 360:
            return 0, 0
    def try_move(self, angle):
        pos = self.look_at(angle)
        if self.land.isEmpty(pos):
            pos = self.land.findHighestEmpty(pos)
            self.hero.setPos(pos)
        else:
            pos = pos[0], pos[1], pos[2] + 1
            if self.land.isEmpty(pos):
                self.hero.setPos(pos)
    def move_to(self, angle):
        if self.mode == True:
            self.just_move(angle)
        else:
            self.try_move(angle)
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
    def delblock(self,pos):
        blocks = self.findBlocks(pos)
        for block in blocks:
            block.removeNode()

