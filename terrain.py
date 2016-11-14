from pico2d import *
import rollout_2015180042최현욱


global lbound,rbound,ubound,dbound,pivotx,pivoty
lbound=150
rbound=650
ubound=500
dbound=100
pivotx,pivoty=0,0
global stuck
class pannel():
    def __init__(self):

        self.x=0
        self.y=0
        self.surfacey = self.y + 15
        self.surfacel=self.x
        self.surfacer=self.x+105


    def update(self):
        self.x=0-pivotx
        self.y=0-pivoty
        self.surfacey = self.y + 15-pivoty
        self.surfacel = self.x-pivotx
        self.surfacer = self.x + 105-pivotx
        if rollout_2015180042최현욱.player.step==2 and rollout_2015180042최현욱.player.y-rollout_2015180042최현욱.player.jdelt>=self.surfacey:#플랫폼 밟기 처리
            if rollout_2015180042최현욱.player.x>=self.surfacel and rollout_2015180042최현욱.player.x<=self.surfacer:
                rollout_2015180042최현욱.player.y=surface.y+57
                rollout_2015180042최현욱.player.step=0
                rollout_2015180042최현욱.player.jdelt=rollout_2015180042최현욱.player.jmax


