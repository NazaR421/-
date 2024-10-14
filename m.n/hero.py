class Hero():
    def __init__(self,pos,land,):
        self.land=land
        self.hero=loader.loadModel("smiley")
        self.hero.setColor(1,0.5,0)
        self.hero.setScale(0.3)
        self.hero.setPos(pos)
        self.hero.reparentTo(render)
        self.cameraBind()
    def cameraBind(self):
        base.disableMouse()
        base.camera.setH(180)
        base.camera.reparentTo(self.hero)
        base.camera.setPos(0,0,1.5)
        sel.cameraOn = True
    def cameraUp(self):
        base.mouseInterFaceNode.setPos(x,y,z)
        base.camera.reparentTo(render)
        base.enableMouse()
        self.cameraOn=False
