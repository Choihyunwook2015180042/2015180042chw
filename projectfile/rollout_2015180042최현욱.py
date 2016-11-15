from pico2d import *
import Uishowcase
from wall import wall
from Weapon import Disk, WeapoN
import math
from EandO import Pc
from hitdetection import collide
#class definition here{







#플레이어 무빙.
class player:
    def __init__(self):
        self.jumpable=True#prevent multiple jump


        self.x=0
        self.y=107#좌표
        self.watch=1#looking direction
        self.step=0#0=stop,1=jumpup,2=jumpdown
        self.jmax=17#jumpmaxheight
        self.jdelt=17#jump
        self.cnt=0#counting
        self.tick=[0,0,0,0,0,0,0,0]#타격 판정. 머리와 몸통 순서로 좌상우하
        self.framex,self.framey=0,0#프레임.
        self.movecheck=False#키로 인한 좌표변화의 표현
        self.img=load_image('movingbot.png')#로드할 이미지

    def get_bb(self):
        return self.x-50,self.y-62,self.x+49,self.y+61

    def update(self):

        global x,y,watch
        x=self.x
        y=self.y
        watch=self.watch
        if self.movecheck==True:#이동중 애니메이션 표시
            if self.watch==1:#왼쪽 볼 시
                self.framex=0
                self.framey += 1
                if self.framey == 8:
                    self.framey -=1
                    self.tick = [X-45,Y+44,X+30,Y + 9,X-21,Y+6,X+21,Y - 57]
                    self.x-=10
            elif self.watch==2:
                self.framex=1
                self.framey += 1
                if self.framey == 8:
                    self.framey -= 1
                    self.tick = [X-30,Y+44,X+45, Y + 30,X-21,Y+6,X+21,Y - 57]
                    self.x+=10
        elif self.movecheck==False:#정지중 애니메이션 표시
            if self.watch==1:
                self.framex=0
                self.framey=1
                self.tick=[X-22,Y+61,X+48,Y+26,X-3,Y+21,X+33,Y-53]
            else:
                self.framex=1
                self.framey = 0
                self.tick=[X-48,Y+61,X+22,Y+26,X-33,Y+21,X+3,Y-53]

        if self.step==1:
            if self.jdelt<=10:
                self.step=2
                self.walk=False
            else:
                if self.cnt%5 == 0:
                    self.jdelt=self.jdelt/5*4
            self.y+=self.jdelt
            self.cnt += 1

        if self.step==2:
            if self.jdelt>=self.jmax:
                self.jdelt=self.jmax
                self.y -= self.jdelt
            else:
                if self.cnt%5 == 0:
                    self.jdelt = self.jdelt * 2
                self.y -= self.jdelt
                self.cnt += 1
            if self.y-57<=50:#오브젝트 충돌시도 동일처리.추후 낙하판정 들어올시 제거 계획.
                self.y=107
                self.step=0
                self.jumpable=True






    def draw(self):
        self.img.clip_draw(self.framex*100,1116-(124*(self.framey+1)),100,124,self.x,self.y)













#이벤트 핸들러
def handle_events():
    global running
    global x,y
    global mx, my  # 마우스좌표

    events = get_events()
    for event in events:
        if (event.type) == (SDL_MOUSEBUTTONDOWN):
            if event.button == SDL_BUTTON_LEFT:
                if d.ison == False:
                    d.x = event.x
                    d.y = 600 - event.y
                    d.ison = True
            if event.button == SDL_BUTTON_RIGHT:
                if d.ison == True and d.blast == False:
                    if event.x <= d.x + 10 and event.x >= d.x - 10:
                        if (600 - event.y) <= d.y + 10 and (600 - event.y) >= d.y - 10:
                            d.blast = True

        if event.type == SDL_MOUSEMOTION:
            wp.degree = math.atan2((600 - event.y) - 100, event.x - 100)

        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

        elif event.type==SDL_KEYDOWN:
            if event.key==SDLK_a:
                pl.watch=1
                pl.framey=1

                pl.movecheck = True
            elif event.key==SDLK_d:
                pl.watch=2
                pl.framey=1
                pl.movecheck = True
            elif event.type==SDL_KEYUP:
                if event.key==SDLK_a:
                    pl.watch=2
                    pl.framey=1
                if event.key==SDLK_d:
                    pl.watch=1
                    pl.framey=1
        if event.type==SDL_KEYDOWN and event.key==SDLK_SPACE and pl.jumpable==True:
                pl.step=1
                pl.jumpable=False


        elif event.type==SDL_KEYUP:
            if event.key==SDLK_a or event.key==SDLK_d:
                pl.movecheck = False
            if event.key==SDLK_SPACE:
                pl.step=2






    def draw(self):
        self.dis.clip_draw(0, (self.kind + 1) * 21, 21, 21, self.pivx, self.pivy)




#초기화 구역
global step
global X,Y
open_canvas()
pl = player()
ui=Uishowcase.UI()
#####
wl=wall()
wl2=wall()
wp=WeapoN()
d=Disk()
en=Pc()

wl2.x=200
running=True
#게임 루프 구간
while running:
    X,Y=pl.x,pl.y
    handle_events()

    clear_canvas()
    if d.blast==True and d.blasttime==1:
        if pl.x>d.x-100 and pl.x<wl.x+100:
            if pl.y>d.y-100 and pl.y<d.y+100:
                pl.x+=2*((800-pl.x)-(800-d.x))
        if en.x>=d.x-100 and en.x<=d.x+100:
            if en.y>=d.y-100 and en.y<=d.y+100:
                en.x+=2*((800-en.x)-(800-d.x))
                print('collide')

    if pl.movecheck==True and pl.tick[4]>wl.x-10 and pl.tick[4]<wl.x+10 and pl.y<wl.y+52 and pl.y>wl.y-52:
        pl.movecheck=False
        pl.x-=20
    elif pl.movecheck==True and pl.tick[6]>wl.x-10 and pl.tick[6]<wl.x+10 and pl.y<wl.y+52 and pl.y>wl.y-52:
        pl.movecheck = False
        pl.x += 20






    if pl.x>en.x-50 :
        if pl.x<en.x+50 :
            if pl.y<=en.y+49 :
                if pl.y>=en.y-49:
                    en.state=1







    pl.update()

    d.update()
    wp.x=pl.x
    wp.y=pl.y



    en.draw()
    wl.draw()
    ui.draw()
    pl.draw()
    wp.draw()
    d.draw()


    update_canvas()


    delay(0.01)


#종료 코드

close_canvas()