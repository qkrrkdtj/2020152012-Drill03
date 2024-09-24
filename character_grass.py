from pico2d import *
import math

open_canvas()

# fill here
grass = load_image('grass.png')
boy = load_image('character.png')

def draw_boy(x, y):
    clear_canvas_now()
    boy.draw_now(x, y)
    delay(0.1)

def run_top():
    print('TOP')
    
    for x in range(0, 800, 10):
        draw_boy(x,550)
    pass

def run_right():
    print('RIGHT')

    for y in range(550, 60, -10):
        draw_boy(800, y)
        
    pass

def run_bottom():
    print('BOTTOM')

    for x in range(800, 0, -10):
        draw_boy(x, 60)
        
    pass

def run_left():
    print('LEFT')

    for y in range(60, 550, 10):
        draw_boy(0, y)
        
    pass

def run_rectangle():
    print('RECTANGLE')

    run_top()
    run_right()
    run_bottom()
    run_left()
    
    pass

def run_circle():
    print('CIRCLE')

    r, cx, cy = 300, 800 // 2, 600 // 2

    for d in range(0, 360):
        x = r * math.cos(math.radians(d)) + cx
        y = r * math.sin(math.radians(d)) + cy
        
        draw_boy(x, y)
    
    pass

def run_leftside():
    print('LEFTSIDE')

    for i in range(0, 300, 10):
        x = i+100
        y = i*2

        draw_boy(x, y)

def run_rightside():
    print('RIGHTSIDE')
    x, y = 400, 600
    
    while(x<600):
        x = x+10
        y = y-20
        

        draw_boy(x, y)

def run_triangle():
    print('TRIANGLE')

    run_leftside()
    run_rightside()
    run_bottom()

    pass

while True:
    run_circle()
    run_rectangle()
    run_triangle()
    break


close_canvas()
