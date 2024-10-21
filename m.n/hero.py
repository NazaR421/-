key_switch_camera='c'
key_switch_mode='z'

key_forward='w'
key_back='s'
key_right='a'
key_up="e"
key_down='q'

key_turn_left='n'
key_turn_right='m'
class Hero():
    def __init__(self,pos,land):
        self.land = land
        self.mode=True
        self.hero = loader.loadModel('smiley')
        self.hero.setColor(1, 0.5, 0)
        self.hero.setScale(0.3)
        self.hero.setPos(pos)
        self.hero.reparentTo(render)
        self.accept_events()
        self.cameraBind()
    def cameraBind(self):
        base.disableMouse()
        base.camera.setH(180)
        base.camera.reparentTo(self.hero)
        base.camera.setPos(0, 0, 1.5)
        self.cameraOn = True

    def cameraUp(self):
        pos = self.hero.getPos()
        base.mouseInterfaceNode.setPos(-pos[0], -pos[1], -pos[2]-3)
        base.camera.reparentTo(render)
        base.enableMouse()
        self.cameraOn = False

    def changeView(self):
        if self.cameraOn:
            self.cameraUp()
        else:
            self.cameraBind()

    def accept_events(self):
        base.accept('c', self.changeView)
        base.accept('n',self.turn_left)
        base.accept('n'+'-repeat',self.turn_left)
        base.accept('m',self.turn_right)
        base.accept('m'+'-repeat',self.turn_right)
         
    def turn_left(self):
        self.hero.setH((self.hero.getH()+5)%360)
    def turn_right(self):
        self.hero.setH((self.hero.getH()-5)%360)
    def look_at(self,angle):
        x_from=round(self.hero.getX())
        y_from=round(self.hero.getY())
        Z_from=round(self.hero.getZ())

        dx,dy=self.check_dir(angle)
        x_to=x_from+dx
        y_to=y_from+dy
        return x_to,y_to,z_from
