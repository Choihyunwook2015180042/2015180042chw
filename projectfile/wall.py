from pico2d import *






class wall:
    tile=None
    def __init__(self):
        self.x=400
        self.y=100
        if self.tile==None:
            self.tile=load_image('ezwall.png')


    def get_bb(self):
        return self.x-10,self.y-52,self.x+10,self.y+52

    def draw(self):
        self.tile.draw(self.x-10,self.y)
        self.tile.draw(self.x+10,self.y)