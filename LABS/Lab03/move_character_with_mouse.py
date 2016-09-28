from pico2d import *

def handle_events():
    global running
    global x, y
    global radius
    events = get_events()
    for event in events:
        if event.type==SDL_QUIT:
            running=False
        elif event.type==SDL_KEYDOWN:
            if event.key==SDLK_ESCAPE:
                running=False
            elif event.key==SDLK_a:
                if radius>=300:
                    radius=radius
                else:
                    radius+=20
            elif event.key==SDLK_d:
                if radius<=20:
                    radius=radius
                else:
                    radius-=20
            elif event.key==SDLK_LEFT:
                if x >= 0:
                    x-=20
            elif event.key==SDLK_RIGHT:
                if x<=800:
                    x+=20
            elif event.key==SDLK_UP:
                if y<=600:
                    y+=20
            elif event.key==SDLK_DOWN:
                if y>=0:
                    y-=20
        elif event.type==SDL_MOUSEBUTTONDOWN:
                x, y= event.x, 600-event.y


    pass



open_canvas()
grass = load_image('grass.png')
character = load_image('run_animation.png')

x=400
y=300
radius=100
degree=15

a = x + radius * math.cos(degree)
b = y + radius * math.sin(degree)
running = True
frame = 0
while (running):
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(frame * 100, 0, 100, 100, a, b)
    update_canvas()
    frame = (frame + 1) % 8
    a = x + radius * math.cos(degree)
    b = y + radius * math.sin(degree)
    degree+=15
    delay(0.01)
    handle_events()

close_canvas()




