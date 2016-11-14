from pico2d import *

global unlock_weapon
class UI:
    def __init__(self):
        self.x,self.y=68,23
        self.slot = load_image('UI_itemslot.png')
        self.main=load_image('UI_main.png')






    def draw(self):
        self.main.draw(400,23)
        self.slot.draw(self.x,self.y)


