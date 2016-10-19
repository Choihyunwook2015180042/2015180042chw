from pico2d import *
import rollout_2015180042최현욱
import math

class shooter():
    def __init__(self):
        global main,DofM
        main=rollout_2015180042최현욱()
        self.x,self.y=0,0


    def update(self):
        if(main.player.watch==1):
            if(main.player.movecheck==False):
                self.x, self.y = main.player.x+18, main.player.y+6
            else:
                self.x, self.y = main.player.x, main.player.y - 12
        elif (main.player.watch==2):
            if (main.player.movecheck == False):
                self.x, self.y = main.player.x - 18, main.player.y - 6
            else:
                self.x, self.y = main.player.x, main.player.y + 12




class Tan():
    def __init__(self):
        self.pivx,self.pivy=0,0


