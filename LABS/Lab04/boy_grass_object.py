import random
from pico2d import *

# Game object class here
class Boy:
    def __init__(self):
        self.x, self.y = random.randint(0,500) , 90
        self.frame = 0
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = random.randint(0,7)
        self.frame = (self.frame+1)%8
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame*100,0,100,100,self.x,self.y)

class Ball:
    def __init__(self):
        self.x,self.y=random.randint(0,800),600
        self.image=load_image('ball.png')

    def update(self):
        if(self.y>50):
            self.y -= random.randint(5,10)

    def draw(self):
        self.image.draw(self.x,self.y)

class Grass:
    def __init__(self):
        self.image=load_image('grass.png')

    def draw(self):
        self.image.draw(400,30)

def handle_events():
    global running

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

# init
open_canvas()

team=[Boy() for i in range(11)]
balls=[Ball()for i in range(20)]
grass=Grass()

running=True;


# game_loop
while running:
    handle_events()
    for boy in team:
        boy.update()
    for ball in balls:
        ball.update()
    clear_canvas()
    grass.draw()
    for boy in team:
        boy.draw()
    for ball in balls:
        ball.draw()
    update_canvas()

    delay (0.05)


# when shutdown
close_canvas()