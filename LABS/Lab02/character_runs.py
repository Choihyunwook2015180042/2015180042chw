from pico2d import *
open_canvas()
grass = load_image('grass.png')
character = load_image('run_animation.png')
cham=load_image('cham.png')

x = 0
frame=0
while(x<800):
    clear_canvas()
    grass.draw(400,30)
    character.clip_draw(frame*100,0,100,100,x,90)
    cham.draw(x-80,130)
    update_canvas()
    frame=(frame+1)%8
    x+=5
    delay(0.05)
    get_events()

close_canvas()

