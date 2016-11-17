from pico2d import *


##타이틀화면의 관리.
##애니메이션....넣는게 좋을까.
##마우스 좌표 체크해야지...
class faceimage:
    mimage = None
    kpusign=None
    startbutton=None
    loadbutton=None
    quitbutton=None
    def __init__(self):
        if self.mimage==None:
            self.mimage=load_image('titlescreen-noanim.png')
        if (self.startbutton, self.loadbutton, self.quitbutton)==(None, None, None):
            self.startbutton=load_image('titleanimation.png')
            self.loadbutton = load_image('titleanimation.png')
            self.quitbutton = load_image('titleanimation.png')



    def showmainpage(self):
        if self.kpusign != None:
            self.kpusign.draw(401,301)
            delay(2)
            self.kpusign=None
        self.mimage.draw(401,301)


