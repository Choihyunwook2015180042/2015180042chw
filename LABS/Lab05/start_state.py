import game_framework
from pico2d import *


name = "StartState"
image = None
logo_time = 0.0


def enter():
    global image
    open_canvas()
    image=load_image('kpu.credit.png')
    pass


def exit():
    global image
    del(image)
    close_canvas()
    pass


def update():
    pass


def draw():
    pass




def handle_events():
    events = get_events()
    pass


def pause(): pass


def resume(): pass




