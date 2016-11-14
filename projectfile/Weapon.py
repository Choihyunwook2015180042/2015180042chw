from pico2d import *





class WeapoN:
    visual = None
    def __init__(self):
        self.degree=0
        self.x=0
        self.y=107
        if self.visual==None:
            self.visual=load_image('diskshooter.png')

    def draw(self):
        self.visual.rotate_draw(self.degree,self.x,self.y)








class Disk:
    shine=None
    bl=None
    def __init__(self):
        self.x=100
        self.y=100
        self.kind=2
        self.ison=False
        self.blast=False
        self.blasttime=0
        self.blmeter=0
        if self.shine==None:
            self.shine=load_image('discs.png')
        if self.bl==None:
            self.bl=load_image('blast.png')




    def update(self):
        if self.blast==True:
            self.blasttime+=1
            if self.blasttime%2==1:
                self.blmeter+=1
            if self.blasttime==10:
                self.blast=False
                self.ison=False
                self.blasttime=0
                self.blmeter=0

                #visual effect
            #real effect here




    def draw(self):
        if self.ison==True and self.blast==False:
            self.shine.clip_draw(0,self.kind*21,21,21,self.x,self.y)
        elif self.blast==True:
            self.bl.clip_draw(0,(self.blmeter+1)*200,200,200,self.x,self.y)












