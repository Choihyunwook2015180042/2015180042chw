from pico2d import *

def handle_events():
    global running
    global ing
    global vect
    global x
    events = get_events()
    ing=True
    for event in events:
        if event.type==SDL_QUIT:
            running==False
        elif event.type==SDL_KEYDOWN:

            if event.key==SDLK_RIGHT:
                ing=True
                vect=1
            elif event.key==SDLK_LEFT:
                ing=True
                vect=0
            elif event.key==SDLK_ESCAPE:
                running=False
        elif event.type==SDL_KEYUP:
            ing=False
    pass



open_canvas()
grass = load_image('grass.png')
character = load_image('run_animation.png')

running = True
x = 0
frame = 0
while (running):
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(frame * 100, 0, 100, 100, x, 90)
    if ing==True:
        if vect==1:
            x=x+10
        elif vect==0:
            x=x-10
    update_canvas()
    frame = (frame + 1) % 8

    delay(0.05)
    handle_events()

close_canvas()

