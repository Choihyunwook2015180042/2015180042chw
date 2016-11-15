from pico2d import *


class Pc:
    face=None
    def __init__(self):
        self.x=600
        self.y=88
        self.state=0
        if self.face==None:
            self.face=load_image('btype.png')



    def draw(self):
        self.face.clip_draw(0,self.state*100,100,100,self.x, self.y)






